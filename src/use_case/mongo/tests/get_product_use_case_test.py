import pytest

from unittest.mock import Mock

from src.use_case.mongo.get_product_use_case import GetProductMongoUseCase

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from .data.get_product_use_case_data import get_product_sucessfully, get_product_not_found, get_product_product_without_image, get_product_with_int_code

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = GetProductMongoUseCase(repository)

    return repository, use_case


def test_get_product_sucessfully(setup_use_case):

    data = get_product_sucessfully()

    repository, use_case = setup_use_case

    repository.get_product_by_code.return_value = data["get_product_by_code"]

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200

    repository.get_product_by_code.assert_called_once_with(data["params"]["code"])


def test_get_product_not_found(setup_use_case):

    data = get_product_not_found()

    repository, use_case = setup_use_case

    repository.get_product_by_code.return_value = None

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpNotFound):

        use_case.handle(http_request)
    
    repository.get_product_by_code.assert_called_once_with(data["params"]["code"])


def test_get_product_product_without_image(setup_use_case):

    data = get_product_product_without_image()

    repository, use_case = setup_use_case

    repository.get_product_by_code.return_value = data["get_product_by_code"]

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert response.body == data["expected_body"]
    assert response.status_code == 200

    repository.get_product_by_code.assert_called_once_with(data["params"]["code"])


def test_get_product_with_int_code(setup_use_case):

    data = get_product_with_int_code()

    repository, use_case = setup_use_case

    repository.get_product_by_code.return_value = None

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpUnprocessableEntity):

        use_case.handle(http_request)

    repository.get_product_by_code.assert_not_called()
