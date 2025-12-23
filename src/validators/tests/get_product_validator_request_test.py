import pytest

from src.validators.get_product_validator_request import get_product_validator_request

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def test_validator_schema_return_sucessfully():

    params = {
        "code": "123"
    }

    get_product_validator_request(params)


def test_validator_schema_with_wrong_input_type():

    params = {
        "code": 123 #Must be string
    }

    with pytest.raises(HttpUnprocessableEntity):

        get_product_validator_request(params)


def test_validator_schema_with_empty_field():

    params = {
        "code": ""
    }

    with pytest.raises(HttpUnprocessableEntity):

        get_product_validator_request(params)