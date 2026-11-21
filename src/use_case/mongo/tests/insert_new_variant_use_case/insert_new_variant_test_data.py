import os

import copy

from datetime import datetime

from bson.objectid import ObjectId

from unittest.mock import ANY

from src.utils.image_type import image_string

def valid_setup():

    params = {
        "code": "10"
    }

    body = {
        "description": "Product C",
        "stock": 50,
        "image": image_string,
        "brand": "Lacta",
        "reference": "Lac 500",
        "location": ["C01"],
        "measure": "Unidate",
        "keepBuying": False,
        "quantity_change": 50,
        "warehouse":{
            "quantity_change": 15,
            "measure": "Caixa",
            "stock": 15,
            "location":["P1"],
            "last_change": datetime.now()
        }
    }

    response_attributes = {
        "_id": ANY,
        **copy.deepcopy(body),
        "last_change": ANY,
    }

    del response_attributes["image"]

    response_attributes["warehouse"]["last_change"] = ANY

    expected_response = {
        "data":{
            "operation": "Insert",
            "count": 1,
            "attributes": response_attributes
        }
    }

    entity_create = {
        "_id": ObjectId(),
        **body,
        "last_change": ANY
    }

    data = {
        "params": params,
        "body": body,
        "expected_response": expected_response,
        "host": os.getenv("HOST"),
        "entity_create": entity_create
    }

    return data


def insert_variant_in_a_product_that_not_exists_data():


    data = valid_setup()

    params = data["params"]

    body = data["body"]
    
    data = {
        "params": params,
        "body": body
    }

    return data


