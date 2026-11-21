import pytest

from unittest.mock import Mock

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_unavailable_service import HttpUnavailableService

from insert_new_variant_test_data import valid_setup, insert_variant_in_a_product_that_not_exists_data
from src.use_case.mongo.insert_new_variant_use_case import InsertNewVariantMongoUseCase

@pytest.fixture
def setup_use_case():

    repository = Mock()
    entity = Mock()

    use_case = InsertNewVariantMongoUseCase(repository, entity)

    return repository, use_case, entity


def test_insert_variant_successfully(setup_use_case):

    data = valid_setup()

    repository, use_case, entity = setup_use_case

    params = data["params"]
    body = data["body"]
    host = data["host"]

    repository.check_if_product_exists.return_value = True
    entity.create.return_value = data["entity_create"]

    http_request = HttpRequest(body=body, params=params, header=host)

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)

    assert response.body == data["expected_response"]
    assert response.status_code == 201

    code = params["code"]

    repository.check_if_product_exists.assert_called_once_with(code)
    repository.insert_new_variant.assert_called_once_with(code, data["entity_create"])


def test_insert_variant_in_a_product_that_not_exists(setup_use_case):

    data = insert_variant_in_a_product_that_not_exists_data()

    repository, use_case, entity = setup_use_case

    repository.check_if_product_exists.return_value = False

    params = data["params"]
    body = data["body"]

    http_request = HttpRequest(body=body, params=params)

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)

    code = params["code"]


    repository.check_if_product_exists.assert_called_once_with(code)
    repository.insert_new_variant.assert_not_called()
    entity.create.assert_not_called()


def test_error_unavailable_service(setup_use_case):

    data = valid_setup()

    repository, use_case, entity = setup_use_case

    http_request = HttpRequest(params=data["params"], body=data["body"])

    repository.check_if_product_exists.side_effect = HttpUnavailableService("Error: Database Unavailable")

    with pytest.raises(HttpUnavailableService):
        use_case.handle(http_request)

    code = data["params"]["code"]

    entity.create.assert_not_called()
    repository.check_if_product_exists.assert_called_once_with(code)
    repository.insert_new_variant.assert_not_called()
    
    

