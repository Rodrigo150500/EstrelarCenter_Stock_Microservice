from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest
from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from .product_repository import ProductRepositoryMongo

from src.errors.types.http_not_found import HttpNotFound

from .data.product_repository_integration_data import insert_product_variant_data, insert_new_variant_in_product_exist_data, update_product_variant_data, check_if_product_exists_data
mongo_db_connection.connect()


@pytest.fixture
def setup_repository():

    connection = mongo_db_connection.get_db_connection()
    
    repository = ProductRepositoryMongo(connection)

    return repository


@pytest.mark.skip()
def test_insert_product(setup_repository):

    data = insert_product_variant_data()

    repository = setup_repository

    response = repository.insert_product(data)
    
    assert response.inserted_id is not None
    assert response.acknowledged == True


@pytest.mark.skip()
def test_insert_new_variant_in_product_exist(setup_repository):

    data = insert_new_variant_in_product_exist_data()

    repository = setup_repository

    response = repository.insert_new_variant("10", data)

    assert response.acknowledged == True
    assert response.matched_count == 1
    assert response.modified_count == 1


@pytest.mark.skip()
def test_get_product_by_code_return_product(setup_repository):

    repository = setup_repository

    product = repository.get_product_by_code("10")

    assert product is not None


@pytest.mark.skip()
def test_get_product_by_code_return_error_not_found(setup_repository):

    repository = setup_repository

    with pytest.raises(HttpNotFound):
        repository.get_product_by_code("aaa")


@pytest.mark.skip()
def test_update_product_variant(setup_repository):

    data = update_product_variant_data()

    repository = setup_repository

    product = repository.get_product_by_code("10")

    object_id = product["variants"][0]["_id"]

    code = "10"

    response = repository.update_product_variant_by_object_id(code, object_id, data)

    assert response.acknowledged == True
    assert response.matched_count == 1
    assert response.modified_count == 1


@pytest.mark.skip()
def test_get_all_products(setup_repository):

    repository = setup_repository

    response = repository.get_all_products()

    assert len(response) > 0


@pytest.mark.skip()
def test_remove_item(setup_repository):

    repository = setup_repository

    product = repository.get_product_by_code("10")

    object_id = product["variants"][0]["_id"]

    response = repository.remove_variant_by_object_id("10", object_id)

    assert response.matched_count == 1
    assert response.acknowledged ==  True
    assert response.modified_count == 1


@pytest.mark.skip()
def test_remove_product(setup_repository):

    repository = setup_repository

    response = repository.delete_product_by_code("10")


    assert response.acknowledged == True
    assert response.deleted_count == 1


@pytest.mark.skip()
def test_check_if_variant_exists_data(setup_repository):

    repository = setup_repository

    code = "10"
    object_id = "6953c87972d481a4b87b65d1"

    response = repository.check_if_variant_exists(code, object_id)

    assert response == True


@pytest.mark.skip()
def test_check_if_product_exists(setup_repository):

    data = check_if_product_exists_data()

    repository = setup_repository

    repository.insert_product(data["fields"])

    code = "10"

    repository.check_if_product_exists(code)


@pytest.mark.skip()
def test_check_if_product_not_exists(setup_repository):

    repository = setup_repository

    code = "100"

    with pytest.raises(HttpNotFound):
        repository.check_if_product_exists(code)

from bson.binary import Binary
def test_get_image_variant_sucessfully(setup_repository):
    
    repository = setup_repository

    image = repository.get_variant_image_by_code("10", "6955894b90cd6b2cf5422628")    

    print(image), Binary

    assert isinstance(image, bytes)