import pytest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.validators.get_product_image_validator_request import get_image_product_validator_request


def test_get_image_sucessfully():

    params = {
        "code": "123",
        "_id": "68b70ef826423e500863c1c7"
    }

    get_image_product_validator_request(params)


def test_wrong_id_return_HttpUnprocessableEntity():

    params = {
        "code": "123",
        "_id": "123ABC"
    }

    with pytest.raises(HttpUnprocessableEntity):
        get_image_product_validator_request(params)