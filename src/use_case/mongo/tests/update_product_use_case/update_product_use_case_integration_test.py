from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest

from update_product_use_case_integration_data import update_product_sucessfully_data, update_second_variant_sucessfully_data, update_product_not_found_data

from src.use_case.mongo.update_product_use_case import UpdateProductMongoUseCase
from src.domain.entity.product_entity import ProductEntity
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.model.mongo.settings.mongo_db_connection import mongo_db_connection


from update_product_use_case_integration_data import setup_use_case_data

from src.errors.types.http_not_found import HttpNotFound

from src.main.http_types.http_request import HttpRequest

@pytest.fixture
def setup_use_case():
    print("ola")
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
        pass
        # repository.delete_product_by_code(code="10")

def test_update_product_sucessfully(setup_use_case):
    return
    use_case, object_id, _, repository = setup_use_case

    data = update_product_sucessfully_data(object_id)

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    response = use_case.handle(http_request)
   
    assert response.body == data["expected_response"]
    assert response.status_code == 200

    product = repository.get_product_by_code(params["code"])

    assert product["variants"][0]["description"] == body["description"]

@pytest.mark.skip()
def test_update_without_image_successfully(setup_use_case):
    pass

@pytest.mark.skip()
def test_update_with_warehouse_successfully(setup_use_case):
    pass

@pytest.mark.skip()
def test_error_product_not_found_return_error(setup_use_case):
    pass

@pytest.mark.skip()
def test_nothing_to_update_successfully(setup_use_case):
    pass


@pytest.mark.skip()
def test_unavailable_database_return_error(setup_use_case):
    pass
