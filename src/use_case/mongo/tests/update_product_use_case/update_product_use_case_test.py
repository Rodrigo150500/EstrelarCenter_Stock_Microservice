import os

from dotenv import load_dotenv

load_dotenv("dev.env")

import pytest

from unittest.mock import Mock, ANY

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_internal_server_error import HttpInternalServerError

from src.use_case.mongo.update_product_use_case import UpdateProductMongoUseCase

from src.use_case.mongo.tests.update_product_use_case.update_product_use_case_test_data import update_product_sucessfully_data

PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

@pytest.fixture
def setup_use_case():

    repository = Mock()
    product_entity = Mock()
    
    use_case = UpdateProductMongoUseCase(repository, product_entity)

    return repository, product_entity, use_case


def test_update_product_sucessfully(setup_use_case):

    #Arrange
    data = update_product_sucessfully_data()

    repository, product_entity, use_case = setup_use_case

    params = data["params"]
    body = data["body"]

    code = params["code"]
    _id = params["_id"]

    http_request = HttpRequest(params=params, body=body, header=f"{HOST}:{PORT}")

    repository.check_if_variant_exists.return_value = True
    repository.get_variant_by_code_and_id.return_value = data["get_variant_by_code_and_id"]

    product_entity.update.return_value = data["entity_update"]

    #Act
    response = use_case.handle(http_request)

    #Assert
    assert response.status_code == 200
    assert response.body == data["expect_response"]

    repository.check_if_variant_exists.assert_called_once_with(code, _id)
    repository.get_variant_by_code_and_id.assert_called_once_with(code, _id)
    repository.update_product_variant_by_object_id.assert_called_once_with(code, _id, data["assert_called_product_repository_update"])

    product_entity.update.assert_called_once_with(body)
    

def test_update_without_image_successfully(setup_use_case):
    pass
    #Arrange
    
    # data = valid_setup()

    # repository, product_entity, use_case = setup_use_case

    # params = data["params"]
    # body = data["body"]

    # del body["image"]

    # code = params["code"]
    # _id = params["_id"]

    # http_request = HttpRequest(params=params, body=body, header=f"{HOST}:{PORT}")

    # repository.check_if_variant_exists.return_value = True
    # repository.get_variant_by_code_and_id.return_value = data["get_variant_by_code_and_id"]

    # product_entity.update.return_value = data["entity_update"]

    # #Act
    # response = use_case.handle(http_request)




def test_update_with_warehouse_successfully():
    pass


def test_error_product_not_found_return_error():
    pass


def test_nothing_to_update_successfully():
    pass


def test_unavailable_database_return_error():
    pass

