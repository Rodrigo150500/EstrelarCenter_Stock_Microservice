from unittest.mock import ANY

from src.utils.image_type import image_string

def insert_variant_successfully_data():

    params = {
        "code": "10"
    }

    product = {
        "description": "Product C",
        "stock": 50,
        "image": image_string,
        "brand": "Lacta",
        "reference": "Lac 500",
        "location": "C01",
        "measure": "Unidate",
        "keepBuying": False,
        "quantity_change": 50,
    }

    response_attributes = {
        "_id": ANY,
        **product,
        "last_change": ANY,
    }

    del response_attributes["image"]

    expected_response = {
        "data":{
            "operation": "Insert",
            "count": 1,
            "attributes": response_attributes
        }
    }

    data = {
        "params": params,
        "product": product,
        "expected_response": expected_response
    }

    return data


def insert_variant_in_a_product_that_not_exists_data():

    params = {
        "code": "123ABC"
    }

    product = {
        "description": "Product C",
        "stock": 50,
        "image": image_string,
        "brand": "Lacta",
        "reference": "Lac 500",
        "location": "C01",
        "measure": "Unidate",
        "keepBuying": False,
        "quantity_change": 50,
    }

    data = {
        "params": params,
        "product": product
    }

    return data

def wrong_body_schema_data():

    params = {
        "code": "10"
    }

    product = {
        "description": "Product C",
        "stock": "50", #Must be integer
        "image": image_string,
        "brand": "Lacta",
        "reference": "Lac 500",
        "location": "C01",
        "measure": "Unidate",
        "keepBuying": "False", #Must be boolean
        "quantity_change": 50,
    }

    data = {
        "params": params,
        "product": product
    }

    return data