import pytest

from unittest.mock import Mock

from src.use_case.mongo.insert_product_use_case import InsertProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from insert_product_use_case_test_data import insert_product_sucessfully, insert_product_with_int_code, insert_product_that_already_exists

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_conflict import HttpConflict
from src.errors.types.http_not_found import HttpNotFound

@pytest.fixture
def setup_use_case():

    repository = Mock()

    use_case = InsertProductMongoUseCase(repository)

    return repository, use_case


def test_insert_product_sucessfully(setup_use_case):

    data = insert_product_sucessfully()

    repository, use_case = setup_use_case

    http_request = HttpRequest(body=data["body"])

    repository.get_product_by_code.side_effect = HttpNotFound("Product not found")

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

    repository.get_product_by_code.return_value = data["get_product_by_code"]

    http_request = HttpRequest(body=data["body"])

    with pytest.raises(HttpConflict):

        use_case.handle(http_request)

    repository.get_product_by_code.assert_called_once_with(data["body"]["code"])
    repository.insert_product_item.assert_not_called()
    