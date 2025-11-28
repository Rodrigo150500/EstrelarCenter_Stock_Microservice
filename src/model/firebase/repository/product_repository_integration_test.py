from dotenv import load_dotenv
load_dotenv("dev.env")
import pytest
from .product_repository import ProductRepositoryFirebase
from src.model.firebase.settings.firebase_db_connection import firebase_db_connection

from .data.product_repository_integration_data import insert_product_data, update_product_data

@pytest.fixture
def setup_repository():

    firebase_db_connection.connect()

    connection = firebase_db_connection.get_connection()

    repository = ProductRepositoryFirebase(connection)

    return repository


@pytest.mark.skip()
def test_insert_product_sucessfully(setup_repository):

    data = insert_product_data()

    repository = setup_repository

    response = repository.insert_or_update_product("10", data)

    assert response == True


@pytest.mark.skip()
def test_update_product_sucessfully(setup_repository):

    data = update_product_data()

    repository = setup_repository

    response = repository.insert_or_update_product("10",data)
    
    assert response == True


@pytest.mark.skip()
def test_delete_product_sucessfully(setup_repository):

    repository = setup_repository

    response = repository.delete_product_by_code("10")

    assert response == True
    