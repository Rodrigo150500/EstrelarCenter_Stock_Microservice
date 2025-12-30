from dotenv import load_dotenv
load_dotenv("dev.env")

import os

import pytest

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.insert_product_use_case import InsertProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from .data.insert_product_use_case_integration_data import insert_product_sucessfully, insert_product_that_already_exists

from src.errors.types.http_conflict import HttpConflict

COLLECTION_NAME = os.getenv("COLLECTION_NAME_MONGO_DB_PRODUCTS")

@pytest.fixture
def setup_use_case():
    
    mongo_db_connection.connect()

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = InsertProductMongoUseCase(repository)

    connection.get_collection(COLLECTION_NAME).delete_many({})

    return use_case


def test_insert_product_sucessfully(setup_use_case):

    data = insert_product_sucessfully()

    use_case = setup_use_case

    http_request = HttpRequest(body=data["body"])

    response = use_case.handle(http_request)

    assert response.body == data["expected_body"]
    assert response.status_code == 201


def test_insert_product_that_already_exists(setup_use_case):

    data = insert_product_that_already_exists()

    use_case = setup_use_case

    http_request = HttpRequest(body=data["body"])

    use_case.handle(http_request)

    with pytest.raises(HttpConflict):

        use_case.handle(http_request)