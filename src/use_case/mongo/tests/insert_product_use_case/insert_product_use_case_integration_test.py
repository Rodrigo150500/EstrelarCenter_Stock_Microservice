from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.insert_product_use_case import InsertProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from insert_product_use_case_integration_data import insert_product_sucessfully, insert_product_that_already_exists

from src.errors.types.http_conflict import HttpConflict


@pytest.fixture
def setup_use_case():
    
    try:

        mongo_db_connection.connect()

        connection = mongo_db_connection.get_db_connection()
        repository = ProductRepositoryMongo(connection)
        use_case = InsertProductMongoUseCase(repository)

        yield use_case, repository

    finally:
        repository.delete_product_by_code("10")


def test_insert_product_sucessfully(setup_use_case):

    data = insert_product_sucessfully()

    use_case, repository = setup_use_case

    http_request = HttpRequest(body=data["body"])

    response = use_case.handle(http_request)

    assert response.body == data["expected_body"]
    assert response.status_code == 201

    code = data["body"]["code"]

    product = repository.get_product_by_code(code)

    assert product["code"] == code
    assert product["variants"][0]["description"] == data["body"]["description"]


def test_insert_product_that_already_exists(setup_use_case):

    data = insert_product_that_already_exists()

    use_case, repository = setup_use_case

    http_request = HttpRequest(body=data["body"])

    use_case.handle(http_request)

    with pytest.raises(HttpConflict):

        use_case.handle(http_request)

    code = data["body"]["code"]

    product = repository.get_product_by_code(code)

    assert product["variants"][0]["description"] == data["body"]["description"]