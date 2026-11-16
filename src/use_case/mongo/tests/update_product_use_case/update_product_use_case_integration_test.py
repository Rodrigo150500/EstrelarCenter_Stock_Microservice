from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest

from update_product_use_case_integration_data import update_product_sucessfully_data, update_with_image_successfully_data, update_with_warehouse_successfully_data,error_product_not_found_return_error_data

from src.use_case.mongo.update_product_use_case import UpdateProductMongoUseCase
from src.domain.entity.product_entity import ProductEntity
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.model.mongo.settings.mongo_db_connection import mongo_db_connection


from update_product_use_case_integration_data import setup_use_case_data

from src.errors.types.http_not_found import HttpNotFound

from src.main.http_types.http_request import HttpRequest

@pytest.fixture
def setup_use_case():

    data = setup_use_case_data()

    mongo_db_connection.connect()
    
    connection = mongo_db_connection.get_db_connection()
    product_entity = ProductEntity()
    repository = ProductRepositoryMongo(connection)
    use_case = UpdateProductMongoUseCase(repository, product_entity)
    
    try:

        repository.insert_product(data["product"])
        
        product = repository.get_product_by_code("10")
        
        object_id_1 = str(product["variants"][0]["_id"])
        object_id_2 = str(product["variants"][1]["_id"])
        
        yield use_case, object_id_1, object_id_2, repository

    finally:
        
        repository.delete_product_by_code(code="10")


def test_update_product_sucessfully(setup_use_case):
    
    use_case, object_id_1, _, repository = setup_use_case

    data = update_product_sucessfully_data(object_id_1)

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    response = use_case.handle(http_request)
   
    assert response.body == data["expected_response"]
    assert response.status_code == 200

    code = params["code"]

    product = repository.get_variant_by_code_and_id(code, object_id_1)

    assert product["description"] == body["description"]
    assert product["stock"] == body["stock"]


def test_update_with_image_successfully(setup_use_case):

    use_case, object_id_1, _, repository = setup_use_case

    data = update_with_image_successfully_data(object_id_1)

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    response = use_case.handle(http_request)

    assert response.status_code == 200
    assert response.body == data["expected_response"]

    code = params["code"]

    product = repository.get_variant_by_code_and_id(code, object_id_1)

    assert product["description"] == body["description"]
    assert product["stock"] == body["stock"]
    assert product["image"] == data["image"]


def test_update_with_warehouse_successfully(setup_use_case):

    use_case, object_id_1, _, repository = setup_use_case

    data = update_with_warehouse_successfully_data(object_id_1)

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    response = use_case.handle(http_request)

    assert response.status_code == 200
    assert response.body == data["expected_response"]

    code = params['code']

    product = repository.get_variant_by_code_and_id(code, object_id_1)

    assert product["warehouse"]["stock"] == data["body"]["warehouse"]["stock"]
    assert product["warehouse"]["quantity_change"] == data["body"]["warehouse"]["quantity_change"]
    assert product["warehouse"]["location"] == data["body"]["warehouse"]["location"]


def test_error_product_not_found_return_error(setup_use_case):

    use_case, object_id_1, _, repository = setup_use_case

    data = error_product_not_found_return_error_data(object_id_1)

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    with pytest.raises(HttpNotFound) as exec_info:
        use_case.handle(http_request)

    error = exec_info.value.message

    assert error == "Error: product not found"

    code = "10"

    product = repository.get_variant_by_code_and_id(code, object_id_1)

    assert product["description"] == "Product A"  


@pytest.mark.skip()
def test_nothing_to_update_successfully(setup_use_case):
    pass


@pytest.mark.skip()
def test_unavailable_database_return_error(setup_use_case):
    pass
