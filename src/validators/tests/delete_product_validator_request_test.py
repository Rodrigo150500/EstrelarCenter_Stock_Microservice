import pytest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.validators.delete_product_validator_request import delete_product_validator_request

def test_validate_delete_product_sucessfully():

    params = {
        "code": "123"
    }

    delete_product_validator_request(params)


def test_wrong_input_type():

    params = {
        "code": 123
    }

    with pytest.raises(HttpUnprocessableEntity):
        delete_product_validator_request(params)