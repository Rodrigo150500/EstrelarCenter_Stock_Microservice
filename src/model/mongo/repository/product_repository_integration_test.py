from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest
from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from .product_repository import ProductRepositoryMongo

from .data.product_repository_integration_data import insert_product_item_data, update_product_item_data

mongo_db_connection.connect()


@pytest.fixture
def setup_repository():

    connection = mongo_db_connection.get_db_connection()
    
    repository = ProductRepositoryMongo(connection)

    return repository


@pytest.mark.skip()
def test_insert_product_item(setup_repository):

    data = insert_product_item_data()

    repository = setup_repository

    response = repository.insert_product_item("10", data)
    
    assert response.matched_count == 0
    assert response.modified_count == 0
    assert response.upserted_id is not None


@pytest.mark.skip()
def test_insert_new_item_in_product_exist(setup_repository):

    data = insert_product_item_data()

    repository = setup_repository

    response = repository.insert_product_item("10", data)
    
    assert response.matched_count == 1
    assert response.modified_count == 1


@pytest.mark.skip()
def test_get_all_products(setup_repository):

    repository = setup_repository

    response = repository.get_all_products()

    assert len(response) > 0


@pytest.mark.skip()
def test_update_product_item(setup_repository):

    data = update_product_item_data()

    repository = setup_repository

    response = repository.update_product_item("10",1, data)

    assert response.matched_count == 1
    assert response.modified_count == 1


@pytest.mark.skip()
def test_remove_item(setup_repository):

    repository = setup_repository

    response = repository.remove_item("10",2)

    assert response.matched_count == 1
    assert response.modified_count == 1


@pytest.mark.skip()
def test_remove_product(setup_repository):

    repository = setup_repository

    response = repository.delete_product_by_code("10")

    assert response.deleted_count == 1


