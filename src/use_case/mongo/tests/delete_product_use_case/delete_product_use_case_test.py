import pytest
from unittest.mock import Mock

from src.use_case.mongo.delete_product_use_case import DeleteProductMongoUseCase

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


@pytest.fixture
def setup_use_case():

    repository = Mock()
    
    use_case = DeleteProductMongoUseCase(repository)

    return repository, use_case


def test_delete_product_use_case_sucessfully(setup_use_case):

    repository, use_case = setup_use_case

    http_request= HttpRequest(params={"code": "16"})

    response = use_case.handle(http_request)

    assert response.status_code == 204

    repository.check_if_product_exists.assert_called_once_with("16")
    repository.delete_product_by_code.assert_called_once_with("16")
    

def test_delete_product_use_case_product_not_found(setup_use_case):
    
    repository, use_case = setup_use_case

    http_request = HttpRequest(params={"code": "16"})

    repository.check_if_product_exists.return_value = False

    with pytest.raises(HttpNotFound):

        use_case.handle(http_request)
    
    repository.check_if_product_exists.assert_called_once_with("16")
    repository.delete_product_by_code.assert_not_called()


def test_delete_product_use_case_invalid_params(setup_use_case):
    
    repository, use_case = setup_use_case

    http_request = HttpRequest(params={"code": 123}) #Must be a string code

    with pytest.raises(HttpUnprocessableEntity):

        use_case.handle(http_request)
        
    repository.check_if_product_exists.assert_not_called()
    repository.delete_product_by_code.assert_not_called()
