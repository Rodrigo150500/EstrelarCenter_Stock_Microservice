import pytest

from unittest.mock import Mock

from src.use_case.mongo.insert_product_use_case import InsertProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from insert_product_use_case_test_data import insert_product_sucessfully, insert_product_with_int_code, insert_product_that_already_exists, error_unavailable_service_database_data

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_conflict import HttpConflict
from src.errors.types.http_unavailable_service import HttpUnavailableService

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = InsertProductMongoUseCase(repository)

    return repository, use_case


def test_insert_product_sucessfully(setup_use_case):

    data = insert_product_sucessfully()

    repository, use_case = setup_use_case

    http_request = HttpRequest(body=data["body"])

    repository.check_if_product_exists.return_value = False

    response = use_case.handle(http_request)

    assert response.body == data["expected_body"]
    assert response.status_code == 201


def test_insert_product_with_int_code(setup_use_case):

    data = insert_product_with_int_code()

    repository, use_case = setup_use_case

    http_request = HttpRequest(body=data["body"])

    with pytest.raises(HttpUnprocessableEntity):

        use_case.handle(http_request)

    repository.insert_product_item.assert_not_called()
    repository.get_product_by_code.assert_not_called()


def test_insert_product_that_already_exists(setup_use_case):

    data = insert_product_that_already_exists()
    
    repository, use_case = setup_use_case

    repository.check_if_product_exists.return_value = True

    http_request = HttpRequest(body=data["body"])

    with pytest.raises(HttpConflict):

        use_case.handle(http_request)

    repository.check_if_product_exists.assert_called_once_with(data["body"]["code"])
    repository.insert_product_item.assert_not_called()


def test_error_unavailable_service_database(setup_use_case):

    data = error_unavailable_service_database_data()

    repository, use_case = setup_use_case

    repository.check_if_product_exists.side_effect = HttpUnavailableService("Error: Database Unavailable")

    http_request = HttpRequest(body=data["body"])

    with pytest.raises(HttpUnavailableService):
        use_case.handle(http_request)