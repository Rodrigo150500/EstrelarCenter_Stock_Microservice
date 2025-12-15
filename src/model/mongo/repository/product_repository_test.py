import pytest

from unittest.mock import Mock, call

from .product_repository import ProductRepositoryMongo

from .data.product_repository_data import insert_product_data, insert_new_variant_in_product_exist_data, get_product_by_code_return_product_data

from src.errors.types.http_not_found import HttpNotFound

@pytest.fixture
def setup_repository():

    connection = Mock()
    collection = Mock()

    connection.get_collection.return_value = collection

    repository = ProductRepositoryMongo(connection)

    data = {
        "collection": collection,
        "repository": repository
    }

    return data


def test_insert_product(setup_repository):

    data = insert_product_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.insert_one.return_value = data["insert_one"]

    response = repository.insert_product(data["fields"])

    collection.insert_one.assert_called_once_with(data["fields"])

    assert response == data["insert_one"]


def test_insert_new_variant_in_product_exist(setup_repository):
    
    data = insert_new_variant_in_product_exist_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.update_one.return_value = data["update_one"]

    response = repository.insert_new_variant('10', data["fields"])

    collection.update_one.assert_called_once_with({"code":"10"}, {"$push": {"variants": data["fields"]}})

    assert response == data["update_one"]



def test_get_product_by_code_return_product(setup_repository):
    
    data = get_product_by_code_return_product_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.find_one.return_value = data["find_one"]

    response = repository.get_product_by_code("10")

    collection.find_one.assert_called_once_with({"code":"10"})

    assert response == data["find_one"]


def test_get_product_by_code_return_error_not_found(setup_repository):
    
    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.find_one.return_value = None

    with pytest.raises(HttpNotFound):

        repository.get_product_by_code("10")

    collection.find_one.assert_called_once_with({"code": "10"})
    

def test_update_product_variant(setup_repository):
    pass


def test_get_all_products(setup_repository):
    pass


def test_remove_item(setup_repository):
    pass


def test_remove_product(setup_repository):
    pass
