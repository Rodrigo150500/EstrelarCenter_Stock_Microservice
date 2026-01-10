import pytest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.validators.get_product_by_search_validator_request import get_product_by_search_validator_request


def test_validate_schema_sucessfully():

    params = {
        "search": "chocolate",
        "fields": ["brand", "description"],
        "last_id": "690f84cc001559b2fadc151e"
    }

    get_product_by_search_validator_request(params)


def test_multiple_parameter_to_search_sucessfully():
        
    params = {
        "search": "Chocolate com pimenta",
        "fields": ["brand", "description"],
        "last_id": "690f84cc001559b2fadc151e"
    }

    get_product_by_search_validator_request(params)


def test_with_invalid_schema_should_fail():

    params = {
        "search": "chocolate",
        "fields": "brand", #Must be list
        "last_id": "690f84cc001559b2fadc151e"
    }

    with pytest.raises(HttpUnprocessableEntity):

        get_product_by_search_validator_request(params)


def test_with_invalid_field_name_should_fail():

    params = {
        "search": "chocolate",
        "fields": ["marca"], #Must be "brand, reference or description"
        "last_id": "690f84cc001559b2fadc151e"
    }

    with pytest.raises(HttpUnprocessableEntity):

        get_product_by_search_validator_request(params)


def test_with_invalid_object_id_should_fail():

    params = {
        "search": "chocolate",
        "fields": ["brand", "description"], 
        "last_id": "123ABC" #Must be valid id
    }

    with pytest.raises(HttpUnprocessableEntity):

        get_product_by_search_validator_request(params)


