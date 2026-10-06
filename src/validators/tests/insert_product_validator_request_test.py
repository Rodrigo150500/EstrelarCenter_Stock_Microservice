import pytest

from datetime import datetime

from src.validators.insert_product_validator_request import insert_product_validator_request

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def valid_setup_request():

    body_request = {
            "code": "10",
            "description": "Chocolate Suflair 1kg",
            "brand": "Nestle",
            "reference": "SF-001",
            "location": ["CX01", "CX02"],
            "image": "image string",
            "measure": "Caixa",
            "quantity_change": 5,
            "stock": 10,
            "keepBuying": False,
            "warehouse":{
                "quantity_change": 5,
                "stock": 3,
                "measure": "Caixa",
                "location": ["CX33"]
            }
        }

    return body_request


def test_validator_schema_without_warehouse_insert_return_sucessfully():

    body_request = valid_setup_request()

    del body_request["warehouse"]

    insert_product_validator_request(body_request)


def test_empty_fields_without_warehouse_return_error():

    body_request = valid_setup_request()

    del body_request["warehouse"]

    for key, value in body_request.items():
        body_request[key] = ""

    with pytest.raises(HttpUnprocessableEntity):

        insert_product_validator_request(body_request)      


def test_just_the_required_fields():

    body_request = valid_setup_request()

    del body_request["brand"]
    del body_request["reference"]
    del body_request["location"]
    del body_request["warehouse"]

    insert_product_validator_request(body_request)


def test_fill_the_fields_with_wrong_type_return_error():

    body_request = valid_setup_request()

    body_request["code"] = 10 #Should be string
    body_request["stock"] = "15" #Should be integer
    body_request["keepBuying"] = "False" #Should be boolean


    with pytest.raises(HttpUnprocessableEntity):

        insert_product_validator_request(body_request)      

def test_insert_product_with_warehouse_data():
    pass
    