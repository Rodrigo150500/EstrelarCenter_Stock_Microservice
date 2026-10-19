import pytest
from datetime import datetime

from unittest.mock import Mock, ANY
from bson import ObjectId

from src.use_case.mongo.insert_product_use_case import InsertProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_conflict import HttpConflict
from src.errors.types.http_unavailable_service import HttpUnavailableService


def valid_setup_data():

    data_product = {
        "code": "ABC123",
        "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
        "brand": "Makita",
        "reference": "DHP485RTJ",
        "location": [
            "CX01",
            "P03",
            "CX04"
        ],
        "image": "https://images.example.com/products/dhp485rtj.jpg",
        "measure": "Unidade",
        "quantity_change": 5,
        "stock": 42,
        "keepBuying": True
    }

    data_warehouse = {
        "code": "ABC123",
        "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
        "brand": "Makita",
        "reference": "DHP485RTJ",
        "location": [
            "CX01",
            "P03",
            "CX04"
        ],
        "image": "https://images.example.com/products/dhp485rtj.jpg",
        "measure": "Unidade",
        "quantity_change": 5,
        "stock": 42,
        "keepBuying": True,
        "warehouse": {
            "quantity_change": 1,
            "stock": 4,
            "measure": "Caixa"
        }
    }

    expect_response_product = {
        "data":{
            "operation": "Insert",
            "count": 1,
            "attributes":{
                "_id":ANY,
                **data_product,
                "last_change": ANY
            }
        }
    }

    expect_response_warehouse = {
        "data": {
            "operation": "Insert",
            "count": 1,
            "attributes": {
                "_id": ANY,
                **data_warehouse,
                "last_change": ANY,
                "warehouse":{
                    **data_warehouse["warehouse"],
                    "last_change": ANY
                }
            }
        }
    }

    product_entity_create_product_return = {
        "_id": ObjectId(),
        **data_product,
        "last_change": datetime.now()
    }

    product_entity_create_warehouse_return = {
        "_id": ObjectId(),
        **data_warehouse,
        "last_change": datetime.now(),
        "warehouse": {
            **data_warehouse["warehouse"],
            "last_change": datetime.now()

        }
    }

    del expect_response_product["data"]["attributes"]["image"]
    del expect_response_warehouse["data"]["attributes"]["image"]

    return {
        "warehouse": data_warehouse,
        "product": data_product,
        "product_entity_return": product_entity_create_product_return,
        "warehouse_entity_return": product_entity_create_warehouse_return,
        "expect_product": expect_response_product,
        "expect_warehouse": expect_response_warehouse
    }


@pytest.fixture
def setup_use_case():

    repository = Mock()
    product_entity = Mock()

    use_case = InsertProductMongoUseCase(repository, product_entity)

    return repository, use_case, product_entity


def test_insert_product_successfully(setup_use_case):

    data = valid_setup_data()
    data_product = data["product"]

    product_entity_return = data["product_entity_return"]

    repository, use_case, product_entity = setup_use_case

    http_request = HttpRequest(body=data_product)
    expect_response = data["expect_product"]

    repository.check_if_product_exists.return_value = False
    product_entity.create.return_value = product_entity_return

    response = use_case.handle(http_request)

    assert response.body == expect_response
    assert response.status_code == 201
    
    repository.insert_product.assert_called_once()
    product_entity.create.assert_called_once_with(data_product)


def test_product_with_warehouse_successfully(setup_use_case):


    data = valid_setup_data()
    data_product = data["warehouse"]

    product_entity_return = data["warehouse_entity_return"]

    repository, use_case, product_entity = setup_use_case

    http_request = HttpRequest(body=data_product)
    expect_response = data["expect_warehouse"]

    repository.check_if_product_exists.return_value = False
    product_entity.create.return_value = product_entity_return

    response = use_case.handle(http_request)

    assert response.body == expect_response
    assert response.status_code == 201
    
    repository.insert_product.assert_called_once()
    product_entity.create.assert_called_once_with(data_product)


def test_insert_product_that_already_exists(setup_use_case):

    data = valid_setup_data()
    data_product = data["product"]
    
    repository, use_case, product_entity = setup_use_case

    repository.check_if_product_exists.return_value = True

    http_request = HttpRequest(body=data_product)

    with pytest.raises(HttpConflict):

        use_case.handle(http_request)

    repository.check_if_product_exists.assert_called_once_with(data_product["code"])
    repository.insert_product_item.assert_not_called()
    product_entity.create.assert_not_called()


def test_error_unavailable_service_database(setup_use_case):

    data = valid_setup_data()
    data_product = data["product"]

    repository, use_case, product_entity = setup_use_case

    repository.check_if_product_exists.side_effect = HttpUnavailableService("Error: Database Unavailable")

    http_request = HttpRequest(body=data_product)

    with pytest.raises(HttpUnavailableService):
        use_case.handle(http_request)

    repository.check_if_product_exists.assert_called_once_with(data_product["code"])
    repository.insert_product_item.assert_not_called()
    product_entity.create.assert_not_called()