import pytest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.validators.remove_item_validator_request import remove_item_validator_request

def test_remove_validator_succesfully():

    params = {
        "code": "10",
        "_id": "68b70ef826423e500863c1c7"
    }

    remove_item_validator_request(params)


def test_remove_validator_with_wrong_object_id():

    params = {
        "code": "10",
        "_id": "abc123"
    }

    with pytest.raises(HttpUnprocessableEntity):
        remove_item_validator_request(params)
