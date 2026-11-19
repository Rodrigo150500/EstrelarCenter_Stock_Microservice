import pytest

from unittest.mock import Mock

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound

from src.use_case.mongo.delete_variant_use_case import DeleteVariantUseCase

from src.use_case.mongo.tests.delete_variant_use_case.delete_variant_use_case_test_data import remove_item_succesfully_data, remove_item_that_not_exists_data, delete_product_with_one_variant_data, removing_one_variant_data

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = DeleteVariantUseCase(repository)

    return repository, use_case


def test_remove_item_succesfully(setup_use_case):

    data = remove_item_succesfully_data()

    http_request = HttpRequest(params=data["params"])

    repository, use_case = setup_use_case

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)

    code = data["params"]["code"]
    object_id = data["params"]["_id"]

    repository.check_if_variant_exists.assert_called_once_with(code, object_id)
    repository.remove_variant_by_object_id.assert_called_once_with(code, object_id)


def test_delete_product_with_one_variant(setup_use_case):

    data = delete_product_with_one_variant_data()

    http_request = HttpRequest(params=data["params"])

    repository, use_case = setup_use_case

    repository.check_if_variant_exists.return_value = data["exists"]
    repository.get_variant_count.return_value = data["get_variant_count"]

    response = use_case.handle(http_request)

    repository.delete_product_by_code.assert_called_once_with(data["params"]["code"])

    assert response.status_code == 204

def test_removing_one_variant(setup_use_case):

    data = removing_one_variant_data()

    http_request = HttpRequest(params=data["params"])

    repository, use_case = setup_use_case

    repository.removing_one_variant.return_value = data["exists"]
    repository.get_variant_count.return_value = data["get_variant_count"]

    response = use_case.handle(http_request)

    code = data["params"]["code"]
    _id = data["params"]["_id"]

    assert isinstance(response, HttpResponse)
    assert response.status_code == 204
    
    repository.remove_variant_by_object_id.assert_called_once_with(code, _id)

    
def test_remove_item_that_not_exists(setup_use_case):

    data = remove_item_that_not_exists_data()

    repository, use_case = setup_use_case

    repository.check_if_variant_exists.side_effect = HttpNotFound("Error: Product Not Found")

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)

    code = data["params"]["code"]
    object_id = data["params"]["_id"]

    repository.check_if_variant_exists.assert_called_once_with(code, object_id)
    repository.remove_variant_by_object_id.assert_not_called()

    