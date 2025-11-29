import pytest
from unittest.mock import Mock

from ..delete_product_use_case import DeleteProductFirebaseUseCase

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from .data.delete_product_use_case_integration_data import delete_product_sucessfully_data

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = DeleteProductFirebaseUseCase(repository)

    data = {
        "repository": repository,
        "use_case": use_case
    }

    return data


def test_delete_product_use_case_sucessfully(setup_use_case):

    data = delete_product_sucessfully_data()

    repository = setup_use_case["repository"]
    use_case = setup_use_case["use_case"]

    http_request = HttpRequest(
        params={
            "code": "123456"
        }
    )

    repository.get_product_by_code.return_value = data["get_product_by_code"]

    response = use_case.handle(http_request)

    assert response.status_code == 204
    assert response.body == data["response_body"]

    repository.get_product_by_code.assert_called_once_with("123456")
    repository.delete_product_by_code.assert_called_once_with("123456")


def test_delete_product_use_case_product_not_found(setup_use_case):

    repository = setup_use_case["repository"]
    use_case = setup_use_case["use_case"]

    http_request = HttpRequest(
        params={
            "code": "999999"
        }
    )

    repository.get_product_by_code.return_value = None

    with pytest.raises(HttpNotFound) as exc_info:
        use_case.handle(http_request)

    assert str(exc_info.value) == "Product not found"

    repository.get_product_by_code.assert_called_once_with("999999")
    repository.delete_product_by_code.assert_not_called()


def test_delete_product_use_case_invalid_params(setup_use_case):

    repository = setup_use_case["repository"]
    use_case = setup_use_case["use_case"]

    http_request = HttpRequest(
        params={
            # "code" is missing
        }
    )

    with pytest.raises(HttpUnprocessableEntity) as exc_info:
        use_case.handle(http_request)


    repository.get_product_by_code.assert_not_called()
    repository.delete_product_by_code.assert_not_called()