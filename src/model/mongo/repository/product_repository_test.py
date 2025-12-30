import pytest

from unittest.mock import Mock, call

from .product_repository import ProductRepositoryMongo

from .data.product_repository_data import insert_product_data, insert_new_variant_in_product_exist_data, get_product_by_code_return_product_data, update_product_variant_data, get_all_products_data, remove_item_data, remove_product_data, check_if_variant_exists_data

from src.errors.types.http_not_found import HttpNotFound

from bson.objectid import ObjectId

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
    
    data = update_product_variant_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.update_one.return_value = data["update_one"]

    object_id = "68b70ef826423e500863c1c7"

    response = repository.update_product_variant_by_object_id("10", object_id, data["fields"])

    assert response == data["update_one"]

    collection.update_one.assert_called_once_with({"code": "10", "variants._id": ObjectId(object_id)}, {"$set": data["fields"]})


def test_get_all_products(setup_repository):
    
    data = get_all_products_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.find.return_value = data["find_one"]

    response = repository.get_all_products()

    assert response == data["find_one"]

    collection.find.assert_called_once_with({})


def test_remove_item(setup_repository):
    
    data = remove_item_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.update_one.return_value = data["update_one"]

    object_id = "68b70ef826423e500863c1c7"

    response = repository.remove_variant_by_object_id("10", object_id)

    assert response == data["update_one"]

    collection.update_one.assert_called_once_with({"code": "10"},{"$pull":{"variants":{"_id": ObjectId(object_id)}}})


def test_remove_product(setup_repository):
    
    data = remove_product_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    collection.delete_one.return_value = data["delete_one"]

    response = repository.delete_product_by_code("10")

    assert response == data["delete_one"]

    collection.delete_one.assert_called_once_with({"code": "10"})


def test_check_if_variant_exists(setup_repository):

    data = check_if_variant_exists_data()

    collection = setup_repository["collection"]
    repository = setup_repository["repository"]

    code = "10"
    object_id = "6953c87972d481a4b87b65d3"

    collection.find.return_value = data["find_one"]

    repository.check_if_variant_exists(code, object_id)

    collection.find_one.assert_called_once_with({"code": code, "variants._id": ObjectId(object_id)},
                {"_id": 1})