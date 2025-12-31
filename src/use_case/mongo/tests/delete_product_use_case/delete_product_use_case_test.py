import pytest
from unittest.mock import Mock

from src.use_case.mongo.delete_product_use_case import DeleteProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from delete_product_use_case_test_data import delete_product_use_case_sucessfully_data

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_internal_server_error import HttpInternalServerError


@pytest.fixture
def setup_use_case():

    repository = Mock()
    
    use_case = DeleteProductMongoUseCase(repository)

    data = {
        "repository": repository,
        "use_case": use_case
    }

    return data


def test_delete_product_use_case_sucessfully(setup_use_case):

    data = delete_product_use_case_sucessfully_data()

    use_case = setup_use_case["use_case"]
    repository = setup_use_case["repository"]

    http_request= HttpRequest(params={"code": "16"})

    response = use_case.handle(http_request)

    assert response.status_code == 200
    assert response.body == data["expected_response"]

    repository.delete_product_by_code.assert_called_once_with("16")
    repository.check_if_product_exists.assert_called_once_with("16")
    

def test_delete_product_use_case_product_not_found(setup_use_case):
    
    use_case = setup_use_case["use_case"]
    repository = setup_use_case["repository"]

    http_request = HttpRequest(params={"code": "9999"})

    repository.check_if_product_exists.side_effect = HttpNotFound("Error: Product not found")

    with pytest.raises(HttpNotFound):

        use_case.handle(http_request)
        

def test_internal_server_error(setup_use_case):

    use_case = setup_use_case["use_case"]
    repository = setup_use_case["repository"]

    repository.check_if_product_exists.side_effect = Exception("Error: Internal Error")

    http_request = HttpRequest(params={"code": "16"})

    with pytest.raises(HttpInternalServerError):
        use_case.handle(http_request)


def test_unavaible_service_error(setup_use_case):
    use_case = setup_use_case["use_case"]
    repository = setup_use_case["repository"]

    repository.check_if_product_exists.side_effect = HttpUnavailableService("Error: Database unavailable")

    http_request = HttpRequest(params={"code": "16"})

    with pytest.raises(HttpUnavailableService):
        use_case.handle(http_request)


def test_delete_product_use_case_invalid_params(setup_use_case):
    
    use_case = setup_use_case["use_case"]

    http_request = HttpRequest(params={"code": 123})

    with pytest.raises(HttpUnprocessableEntity):

        use_case.handle(http_request)

