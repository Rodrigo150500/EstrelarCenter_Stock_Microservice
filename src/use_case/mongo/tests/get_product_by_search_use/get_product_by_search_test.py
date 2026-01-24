import pytest

from unittest.mock import Mock

from src.use_case.mongo.get_product_by_search_use_case import GetProductsBySearchMongoUseCase

from get_product_by_search_test_data import get_product_sucessfully_data, product_not_in_db_return_not_found_data, error_in_database_return_database_unavailable_data, schema_params_should_return_unprocessable_entity_data

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unavailable_service import HttpUnavailableService
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = GetProductsBySearchMongoUseCase(repository)

    return repository, use_case


def test_get_product_sucessfully(setup_use_case):

    data = get_product_sucessfully_data()

    repository, use_case = setup_use_case

    repository.search_by_text.return_value = data["search_by_text"]

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)

    assert response.body == data["expected_response"]
    
    repository.search_by_text.assert_called_once_with(data["pipeline"])


def test_product_not_in_db_return_not_found(setup_use_case):

    data = product_not_in_db_return_not_found_data()

    repository, use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])

    repository.search_by_text.side_effect = HttpNotFound("Error: Product not found")

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)

    repository.search_by_text.assert_called_once()


def test_error_in_database_return_database_unavailable(setup_use_case):

    data = error_in_database_return_database_unavailable_data()

    repository, use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])

    repository.search_by_text.side_effect = HttpUnavailableService("Error: Database unavailable")

    with pytest.raises(HttpUnavailableService):
        use_case.handle(http_request)

    repository.search_by_text.assert_called_once()


def test_schema_params_should_return_unprocessable_entity(setup_use_case):

    data = schema_params_should_return_unprocessable_entity_data()

    repository, use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpUnprocessableEntity):
        use_case.handle(http_request)

    repository.search_by_text.assert_not_called()
