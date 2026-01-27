from datetime import datetime

from bson.objectid import ObjectId

from src.utils.image_type import imagem_bytes, image_string

from unittest.mock import ANY

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

def get_product_sucessfully_data(object_id_1: str, object_id_2: str):

    params = {
        "code": "10"
    }

    expected_response = {
        "data":{
            "operation": "Get",
            "count": 2,
            "attributes":[{
                "_id": ObjectId(object_id_1),
                "description": "Product A",
                "stock": 25,
                "image": image_string,
                "brand": "kit-kat",
                "reference": "kat 500",
                "location": "CX25",
                "measure": "Caixa",
                "keepBuying": True,
                "last_change": ANY,
                "quantity_change": 5
                },{
                    "_id": ObjectId(object_id_2),
                    "description": "Product B",
                    "stock": 50,
                    "image": image_string,
                    "brand": "Bis",
                    "reference": "Bis 150",
                    "location": "C15",
                    "measure": "Unidade",
                    "keepBuying": False,
                    "last_change": ANY,
                    "quantity_change": -10
                }
            ]            
        }
    }

    data = {
        "params": params,
        "expected_response": expected_response
    }

    return data

def get_product_not_found_data():

    params = {
        "code": "14"
    }

    data = {
        "params": params
    }

    return data