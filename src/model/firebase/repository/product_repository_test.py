from dotenv import load_dotenv
load_dotenv("dev.env")

import os
import pytest
from unittest.mock import Mock
from .product_repository import ProductRepositoryFirebase

from .data.product_repository_data import insert_product_data

@pytest.fixture
def setup_repository():

    connection = Mock()
    reference = Mock()

    repository = ProductRepositoryFirebase(connection)

    data = {
        "connection": connection,
        "reference": reference,
        "repository": repository
    }

    return data


def test_insert_product_sucessfully(setup_repository):

    COLLECTION_NAME = os.getenv("COLLECTION_NAME_FIREBASE_PRODUCTS")

    data = insert_product_data()

    connection = setup_repository["connection"]
    repository = setup_repository["repository"]
    reference = setup_repository["reference"]

    connection.reference.return_value = reference

    repository.insert_or_update_product("10", data)

    connection.reference.assert_called_once_with(f"{COLLECTION_NAME}/10")

    reference.update.assert_called_once()


def test_delete_product(setup_repository):

    COLLECTION_NAME = os.getenv("COLLECTION_NAME_FIREBASE_PRODUCTS")

    connection = setup_repository["connection"]
    repository = setup_repository['repository']
    reference = setup_repository["reference"]

    connection.reference.return_value = reference

    repository.delete_product_by_code("10")

    connection.reference.assert_called_once_with(f"{COLLECTION_NAME}/10")

    reference.delete.assert_called_once()