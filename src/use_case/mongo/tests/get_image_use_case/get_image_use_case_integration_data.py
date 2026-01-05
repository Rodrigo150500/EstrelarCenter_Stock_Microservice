from bson.objectid import ObjectId

from src.utils.image_type import imagem_bytes

from datetime import datetime

from src.utils.image_type import image_string

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


def get_image_sucessfully(code, object_id):

    params = {
        "code": code,
        "_id": object_id
    }

    expected_response = {
        "data":{
            "operation": "Get",
            "count": 1,
            "attributes": image_string
        }
    }

    data = {
        "params": params,
        "expected_response": expected_response
    }

    return data


def get_image_not_found():

    params = {
        "code": '16',
        "_id": "64a7f3f5f1c2e3b1a5d6e7f8"
    }

    data = {
        "params": params
    }

    return data