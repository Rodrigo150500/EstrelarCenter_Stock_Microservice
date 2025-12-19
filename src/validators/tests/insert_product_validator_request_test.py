import pytest

from datetime import datetime

from src.validators.insert_product_validator_request import insert_product_validator_request

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def test_validator_schema_insert_return_sucessfully():

    body_request = {
        "code": "10",
        "description": "Chocolate kit-kat 41g",
        "stock": 15,
        "image": "http://192.168.15.36:3000/src/image",
        "brand": "kit-kat",
        "reference": "kit-154",
        "location": "CX15",
        "measure": "Caixa",
        "keepBuying": True,
        "quantity_change": 4
    }

    insert_product_validator_request(body_request)


def test_if_not_fill_the_entire_body_return_error():

    body_request = {
        "code": "",
        "description": "",
        "stock": "",
        "image": "",
        "brand": "",
        "reference": "",
        "location": "",
        "measure": "",
        "keepBuying": "",
        "quantity_change":""

       
    }


    with pytest.raises(HttpUnprocessableEntity):

        insert_product_validator_request(body_request)      


def test_fill_just_the_required_fields():

    body_request = {
        "code": "10",
        "description": "Chocolate kit-kat 41g",
        "stock": 15,
        "image": "http://192.168.15.36:3000/src/image",
        "brand": "",
        "reference": "",
        "location": "",
        "measure": "Caixa",
        "keepBuying": False,
        "quantity_change": -4

    }

    insert_product_validator_request(body_request)


def test_fill_the_fields_with_wrong_type_return_error():

    body_request = {
        "code": 10, #Must be string
        "description": "Chocolate kit-kat 41g",
        "stock": "15", #Must be integer
        "image": "http://192.168.15.36:3000/src/image",
        "brand": "",
        "reference": "",
        "location": "",
        "measure": "Caixa",
        "keepBuying": "False", #Must be boolean
        "quantity_change": "0" #Must be integer

    }

    with pytest.raises(HttpUnprocessableEntity):

        insert_product_validator_request(body_request)      
