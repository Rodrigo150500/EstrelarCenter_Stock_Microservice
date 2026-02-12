from dotenv import load_dotenv

load_dotenv("dev.env")

import pytest

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.insert_new_variant_use_case import InsertNewVariantMongoUseCase

from insert_new_variant_integration_data import setup_use_case_data, insert_variant_succesfully_data, insert_variant_in_a_product_that_not_exists_data

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound


mongo_db_connection.connect()

@pytest.fixture
def setup_use_case():

    data = setup_use_case_data()

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = InsertNewVariantMongoUseCase(repository)
    
    try:

        repository.insert_product(data["product"])

        yield repository, use_case
      
    finally:
        
        repository.delete_product_by_code(data["product"]["code"])


def test_insert_variant_succesfully(setup_use_case):

    data = insert_variant_succesfully_data()

    repository, use_case = setup_use_case

    params = data["params"]
    body = data["product"]

    http_request = HttpRequest(params=params, body=body)

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body == data["expected_response"]

    products = repository.get_product_by_code(data["params"]["code"])["variants"]

    assert len(products) == 3


def test_insert_variant_in_a_product_that_not_exists(setup_use_case):

    data = insert_variant_in_a_product_that_not_exists_data()

    _, use_case = setup_use_case

    params = data["params"]
    body = data["product"]

    http_request = HttpRequest(params=params, body=body)

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)

