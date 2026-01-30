import pytest

from unittest.mock import Mock

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


from insert_new_variant_test_data import insert_variant_successfully_data, insert_variant_in_a_product_that_not_exists_data, wrong_body_schema_data

from src.use_case.mongo.insert_new_variant_use_case import InsertNewVariantMongoUseCase

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = InsertNewVariantMongoUseCase(repository)

    return repository, use_case


def test_insert_variant_successfully(setup_use_case):

    data = insert_variant_successfully_data()

    repository, use_case = setup_use_case

    params = data["params"]
    body = data["product"]

    repository.check_if_product_exists.return_value = True

    http_request = HttpRequest(body=body, params=params)

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.body == data["expected_response"]

    code = params["code"]

    repository.check_if_product_exists.assert_called_once_with(code)
    repository.insert_new_variant.assert_called_once_with(code, body)


def test_insert_variant_in_a_product_that_not_exists(setup_use_case):

    data = insert_variant_in_a_product_that_not_exists_data()

    repository, use_case = setup_use_case

    repository.check_if_product_exists.return_value = False

    params = data["params"]
    body = data["product"]

    http_request = HttpRequest(body=body, params=params)

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)

    code = params["code"]

    repository.check_if_product_exists.assert_called_once_with(code)
    repository.insert_new_variant.assert_not_called()


def test_wrong_body_schema(setup_use_case):

    data = wrong_body_schema_data()

    params = data["params"]
    body = data["product"]

    repository, use_case = setup_use_case

    http_request = HttpRequest(body=body, params=params)

    with pytest.raises(HttpUnprocessableEntity):
        use_case.handle(http_request)

    repository.check_if_product_exists.assert_not_called()
    repository.insert_new_variant.assert_not_called()
