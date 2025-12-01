import pytest
from unittest.mock import Mock

from src.use_case.firebase.insert_product_use_case import InsertProductFirebaseUseCase

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_unavailable_service import HttpUnavailableService

from .data.insert_product_use_case_data import insert_product_sucessfully_data, insert_product_invalid_body, insert_product_database_unavailable_data


@pytest.fixture
def setup_use_case():

    repository = Mock()
    
    use_case = InsertProductFirebaseUseCase(repository)

    data = {
        "use_case": use_case,
        "repository": repository
    }

    return data


def test_insert_product_sucessfully(setup_use_case):

    data = insert_product_sucessfully_data()

    use_case = setup_use_case["use_case"]

    repository = setup_use_case["repository"]

    body = data["body"]

    http_request = HttpRequest(body=body)

    response = use_case.handle(http_request)

    assert response.status_code == 201
    assert response.body == data["expected_response"]

    repository.insert_or_update_product.assert_called_once_with(body["code"] ,data["formatted_body"])

    
def test_insert_product_invalid_body(setup_use_case):

    data = insert_product_invalid_body()

    use_case = setup_use_case["use_case"]

    body = data["body"]

    repository = setup_use_case["repository"]

    http_request = HttpRequest(body=body)

    with pytest.raises(HttpUnprocessableEntity):
        use_case.handle(http_request)

    repository.insert_or_update_product.assert_not_called()


def test_insert_product_database_unavailable(setup_use_case):

    data = insert_product_database_unavailable_data()

    use_case = setup_use_case["use_case"]

    repository = setup_use_case["repository"]

    repository.insert_or_update_product.side_effect = HttpUnavailableService("Database service unavailable")

    body = data["body"]

    http_request = HttpRequest(body=body)

    with pytest.raises(HttpUnavailableService):

        use_case.handle(http_request)

    repository.insert_or_update_product.assert_called_once_with(body["code"] ,data["body_formatted"])








    