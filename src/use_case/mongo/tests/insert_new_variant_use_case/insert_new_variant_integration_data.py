from datetime import datetime

from unittest.mock import ANY

from bson.objectid import ObjectId

from src.utils.image_type import imagem_bytes, image_string

def setup_use_case_data():

    product = {
        "code": "10",
        "variants": [{
            "_id": ObjectId(),
            "description": "Product A",
            "stock": 25,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "kat 500",
            "location": "CX25",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 5
            },{
                "_id": ObjectId(),
                "description": "Product B",
                "stock": 50,
                "image": imagem_bytes,
                "brand": "Bis",
                "reference": "Bis 150",
                "location": "C15",
                "measure": "Unidade",
                "keepBuying": False,
                "last_change": datetime.now(),
                "quantity_change": -10
            }
        ]
    }

    data = {
        "product": product
    }

    return data


def insert_variant_succesfully_data():

    params={
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

    attribute_response = {
        "_id": ANY,
        **product
    }  
    attribute_response["last_change"] = ANY

    del attribute_response["image"]

    expected_response = {
        "data":{
            "operation": "Insert",
            "count": 1,
            "attributes": attribute_response
        }
    }

    data = {
        "params": params,
        "product": product,
        "expected_response": expected_response
    }

    return data

def insert_variant_in_a_product_that_not_exists_data():

    params={
        "code": "ABC" #Must be a existing code in database
    }

    product = {
        "description": "Product not exists",
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