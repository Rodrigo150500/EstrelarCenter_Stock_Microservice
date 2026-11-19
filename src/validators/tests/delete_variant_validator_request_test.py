import pytest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.validators.delete_variant_validator_request import delete_variant_validator_request

def test_validate_delete_product_sucessfully():

    params = {
        "code": "123",
        "_id": "673b8f2a9c4e7d1a5b6f3021"
    }

    delete_variant_validator_request(params)


def test_wrong_input_type():

    params = {
        "code": 123,
        "_id": 456
    }

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        delete_variant_validator_request(params)

    error_list = list(exec_info.value.message.keys())

    assert "_id" in error_list
    assert "code" in error_list

    assert len(error_list) == 2

def test_empty_input():

    params = {
        "code": "",
        "_id": ""
    }

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        delete_variant_validator_request(params)

    error_list = list(exec_info.value.message.keys())

    assert "code" in error_list
    assert "_id" in error_list

    assert len(error_list) == 2

def test_missing_required_fields():

    params = {
        "code": "123"
    }

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        delete_variant_validator_request(params)


    error_list = list(exec_info.value.message)

    assert "_id" in error_list

    assert len(error_list) == 1