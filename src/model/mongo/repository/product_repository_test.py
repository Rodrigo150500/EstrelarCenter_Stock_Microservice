import pytest

from unittest.mock import Mock, call

from .product_repository import ProductRepository

from .data.product_repository_data import get_product_by_code_data, remove_item_data, delete_product_by_code_data, insert_product_item_data, update_product_item_data, get_all_products_data

@pytest.fixture
def setup_repository():

    connection = Mock()
    collection = Mock()

    connection.get_collection.return_value = collection

    repository = ProductRepository(connection)

    data = {
        "collection": collection,
        "repository": repository
    }

    return data


def test_get_product_by_code(setup_repository):

    data = get_product_by_code_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.find_one.return_value = data

    response = repository.get_product_by_code("10")

    collection.find_one.assert_called_once_with({"10":{"$exists": True}})

    assert response == data


def test_remove_item(setup_repository):

    data = remove_item_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.update_one.return_value = data

    call_list = [call({"1": {"$exists": True}}, {"$unset": {f"1.0": 0}})]
    
    response = repository.remove_item("1", 0)

    assert response.matched_count == 1
    assert response.modified_count == 1

    collection.update_one.assert_has_calls(call_list)

    
def test_delete_product_by_code(setup_repository):

    data = delete_product_by_code_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.delete_one.return_value = data

    response = repository.delete_product_by_code("1")

    assert response.deleted_count == 1

    collection.delete_one.assert_called_once_with({"1":{"$exists": True}})


def test_insert_product_item(setup_repository):

    data = insert_product_item_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.update_one.return_value = data["update_one"]

    response = repository.insert_product_item("10", data["fields"])

    assert response.matched_count == 1
    assert response.modified_count == 1

    collection.update_one.assert_called_once_with({"10": {"$exists": True}}, {"$push": {"10": data["fields"]}}, upsert=True)


def test_update_product_item(setup_repository):

    data = update_product_item_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.update_one.return_value = data["update_one"]

    response = repository.update_product_item("10", 0, data['fields'])

    assert response.matched_count == 1
    assert response.modified_count == 1

    collection.update_one.assert_called_once_with({"10.0":{"$exists":True}}, {"$set":{"10.0": data["fields"]}})


def test_get_all_products(setup_repository):

    data = get_all_products_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.find.return_value = data["find"]

    response = repository.get_all_products()

    assert isinstance(response, list)

    collection.find.assert_called_once_with({})