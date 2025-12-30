from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest

from unittest.mock import Mock

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_internal_server_error import HttpInternalServerError

from src.use_case.mongo.update_product_use_case import UpdateProductMongoUseCase

from update_product_use_case_test_data import update_product_sucessfully_data, missing_required_fields_for_body_return_HttpUnprocessableEntity_data, product_not_in_database_return_HttpNotFound_data, database_unavailable_return_HttpUnavailableService_data, update_product_raise_HttpInternalServerError_data


@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = UpdateProductMongoUseCase(repository)

    return repository, use_case


def test_update_product_sucessfully(setup_use_case):

    data = update_product_sucessfully_data()

    repository, use_case = setup_use_case

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(params=params, body=body)

    response = use_case.handle(http_request)

    assert response.body == data["expected_response"]
    assert response.status_code == 200

    code = params["code"]
    object_id = params["_id"]

    repository.check_if_variant_exists.assert_called_once_with(code, object_id)
    repository.update_product_variant_by_object_id.assert_called_once_with(code, object_id, data["body_to_update"])


def test_missing_required_fields_for_body_return_HttpUnprocessableEntity(setup_use_case):

    data = missing_required_fields_for_body_return_HttpUnprocessableEntity_data()

    repository, use_case = setup_use_case

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    with pytest.raises(HttpUnprocessableEntity):
        use_case.handle(http_request)


    repository.check_if_variant_exists.assert_not_called()
    repository.update_product_variant_by_object_id.assert_not_called()


def test_product_not_in_database_return_HttpNotFound(setup_use_case):

    data = product_not_in_database_return_HttpNotFound_data()

    repository, use_case = setup_use_case

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    repository.check_if_variant_exists.side_effect = HttpNotFound("Error: Product Not Found")

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)

    code = params["code"]
    object_id = params["_id"]

    repository.check_if_variant_exists.assert_called_once_with(code, object_id)
    repository.update_product_variant_by_object_id.assert_not_called()


def test_database_unavailable_return_HttpUnavailableService(setup_use_case):

    data = database_unavailable_return_HttpUnavailableService_data()

    repository, use_case = setup_use_case

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    repository.update_product_variant_by_object_id.side_effect = HttpUnavailableService("Error: Database unavailable")

    with pytest.raises(HttpUnavailableService):

        use_case.handle(http_request)

    code = params["code"]
    object_id = params["_id"]
    
    repository.check_if_variant_exists.assert_called_once_with(code, object_id)
    repository.update_product_variant_by_object_id.assert_called_once_with(code, object_id, data["body_to_update"])


def test_update_product_raise_HttpInternalServerError(setup_use_case):
        
    data = update_product_raise_HttpInternalServerError_data()

    repository, use_case = setup_use_case

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    repository.update_product_variant_by_object_id.side_effect = Exception("Error: Unexpected")

    with pytest.raises(HttpInternalServerError):

        use_case.handle(http_request)

    code = params["code"]
    object_id = params["_id"]
    
    repository.check_if_variant_exists.assert_called_once_with(code, object_id)
    repository.update_product_variant_by_object_id.assert_called_once_with(code, object_id, data["body_to_update"])
