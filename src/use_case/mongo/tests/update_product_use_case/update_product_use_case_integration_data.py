from bson.objectid import ObjectId
from datetime import datetime
from src.utils.image_type import imagem_bytes

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

def update_product_sucessfully_data(object_id: str):

    params = {
        "code": "10",
        "_id": object_id
    }

    body = {
        "code": "10",
        "description": "New Description for Update",
        "stock":1000
    }

    expected_response = {
        "data":{
            "operation":"Update",
            "count": 1,
            "attributes": body
        }
    }

    data = {
        "body": body,
        "params": params,
        "expected_response": expected_response
    }

    return data


def update_second_variant_sucessfully_data(object_id: str):

    params = {
        "code": "10",
        "_id": object_id
    }

    body = {
        "code": "10",
        "description": "New product for B",
        "stock":1500,
        "reference": "Lacta"
    }

    expected_response = {
        "data":{
            "operation":"Update",
            "count": 1,
            "attributes": body
        }
    }

    data = {
        "body": body,
        "params": params,
        "expected_response": expected_response
    }

    return data


def update_product_not_found_data():

    params = {
        "code": "1500",
        "_id": str(ObjectId())
    }

    body = {
        "code": "1500",
        "description": "New product for B",
        "stock":1500,
        "reference": "Lacta"
    }

    expected_response = {
        "data":{
            "operation":"Update",
            "count": 1,
            "attributes": body
        }
    }

    data = {
        "body": body,
        "params": params,
        "expected_response": expected_response
    }

    return data