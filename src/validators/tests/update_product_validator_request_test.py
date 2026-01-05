import pytest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.validators.update_product_validator_request import update_product_validator_request

from src.utils.image_type import image_string

def test_validate_update_sucessfully():

    params = {
        "code": "123",
        "_id": "68b70ef826423e500863c1c7"
    }

    body = {
        "code": "123",
        "description": "Product A",
        "stock": 15,
        "image": image_string,
        "brand": "Kit-Kat",
        "reference": "Kit500",
        "location": "CX15",
        "measure": "Unidade",
        "keepBuying": False,
        "quantity_change": -10   
    }

    update_product_validator_request(body, params)


def test_validate_wrong_input_type_return_error():

    params = {
        "code": 123,
        "_id": "68b70ef826423e500863c1c7" #must be string 
    }

    body = {
        "code": 123, #Must be string
        "description": "Product A",
        "stock": 15,
        "image": image_string,
        "brand": "Kit-Kat",
        "reference": "Kit500",
        "location": "CX15",
        "measure": "Unidade",
        "keepBuying": "False", #Must be boolean
        "quantity_change": -10   
    }

    with pytest.raises(HttpUnprocessableEntity):

        update_product_validator_request(body, params)


def test_not_filling_body_return_sucessfully():

    params = {
        "code": "123",
        "_id": "68b70ef826423e500863c1c7" 
    }

    body = {
        "code": "123",
        "description": "",
        "stock": 0,
        "image": "",
        "brand": "",
        "reference": "",
        "location": "",
        "measure": "",
        "keepBuying": False, 
        "quantity_change": 0   
    }

    update_product_validator_request(body, params)