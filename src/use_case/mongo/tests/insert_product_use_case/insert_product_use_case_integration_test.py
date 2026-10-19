from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest

from unittest.mock import ANY

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.insert_product_use_case import InsertProductMongoUseCase
from src.domain.entity.product_entity import ProductEntity

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_conflict import HttpConflict

def valid_setup_data():

    data_product = {
            "code": "10",
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
            "code": "10",
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
                "measure": "Caixa",
                "location": ["CX01"]
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

    del expect_response_product["data"]["attributes"]["image"]
    del expect_response_warehouse["data"]["attributes"]["image"]
    del expect_response_product["data"]["attributes"]["code"]
    del expect_response_warehouse["data"]["attributes"]["code"]

    return {
        "product": data_product,
        "warehouse": data_warehouse,
        "expect_product": expect_response_product,
        "expect_warehouse": expect_response_warehouse
    }


@pytest.fixture
def setup_use_case():
    
    try:
        code = valid_setup_data()["product"]["code"]

        mongo_db_connection.connect()

        product_entity = ProductEntity()
        connection = mongo_db_connection.get_db_connection()
        repository = ProductRepositoryMongo(connection)
        use_case = InsertProductMongoUseCase(repository, product_entity)

        yield use_case, repository

    finally:
        
        repository.delete_product_by_code(code)


def test_insert_product_sucessfully(setup_use_case):

    data = valid_setup_data()
    data_product = data["product"]

    use_case, repository = setup_use_case

    http_request = HttpRequest(body=data_product)

    response = use_case.handle(http_request)

    assert response.body == data["expect_product"]
    assert response.status_code == 201

    code = data_product["code"]

    product = repository.get_product_by_code(code)

    assert product["code"] == code
    assert product["variants"][0]["description"] == data_product["description"]


def test_insert_warehouse_successfully(setup_use_case):

    data = valid_setup_data()
    data_warehouse = data["warehouse"]

    use_case, repository = setup_use_case

    http_request = HttpRequest(body=data_warehouse)

    response = use_case.handle(http_request)

    assert response.body == data["expect_warehouse"]
    assert response.status_code == 201

    code = data_warehouse["code"]

    product = repository.get_product_by_code(code)

    assert product["code"] == code
    assert product["variants"][0]["warehouse"]["stock"] == data_warehouse["warehouse"]["stock"]


def test_insert_product_that_already_exists_return_error(setup_use_case):

    data = valid_setup_data()

    data_product = data["product"]

    use_case, repository = setup_use_case

    http_request = HttpRequest(body=data_product)

    use_case.handle(http_request)

    with pytest.raises(HttpConflict):

        use_case.handle(http_request)

    code = data_product["code"]

    product = repository.get_product_by_code(code)

    assert product["variants"][0]["description"] == data_product["description"]