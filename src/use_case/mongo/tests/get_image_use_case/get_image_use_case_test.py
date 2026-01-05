import pytest

from unittest.mock import Mock

from src.use_case.mongo.get_image_use_case import GetImageMongoUseCase

from get_image_use_case_test_data import get_image_sucessfully_data, get_image_return_product_not_found_data

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFound

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = GetImageMongoUseCase(repository)

    return repository, use_case


def test_get_image_sucessfully(setup_use_case):

    data = get_image_sucessfully_data()

    repository, use_case = setup_use_case

    repository.get_variant_image_by_code.return_value = data["get_product_by_code"]

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert response.status_code == 200

    code = data["params"]["code"]
    object_id = data["params"]["_id"]

    repository.get_variant_image_by_code.assert_called_once_with(code, object_id)


def test_get_image_return_product_not_found(setup_use_case):

    data = get_image_return_product_not_found_data()

    repository, use_case = setup_use_case

    repository.get_variant_image_by_code.return_value = None

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpNotFound):

        use_case.handle(http_request)

    code = data["params"]["code"]
    object_id = data["params"]["_id"]

    repository.get_variant_image_by_code.assert_called_once_with(code, object_id)