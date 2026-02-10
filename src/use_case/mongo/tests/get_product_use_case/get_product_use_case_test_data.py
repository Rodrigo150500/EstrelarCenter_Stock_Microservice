import os
from bson.objectid import ObjectId

from src.utils.image_type import imagem_bytes, image_string

from unittest.mock import ANY

PORT = os.getenv("PORT")

def get_product_sucessfully_data():

    params = {
        "code": "16"
    }

    get_product_by_code = {
        "_id": ObjectId(),
        "code": "16",
        "variants":[{
            "_id": ObjectId(),
            "description": "IMA BORBOLETA C/04",
            "brand": "MAX PING",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": imagem_bytes
        },{
            "_id": ObjectId(),
            "description": "IMA BORBOLETA C/04 A1",
            "brand": "Ima brand",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": imagem_bytes
        }]}
    
    expected_response = {
        "data":{
            "operation": "Get",
            "count": 2,
            "attributes": [{
                "_id": ANY,
                "description": "IMA BORBOLETA C/04",
                "brand": "MAX PING",
                "reference": "16",
                "amount": 0,
                "location": "",
                "last_change": "+4  23/09/2025 17:06:12",
                "stock": 4,
                "measure": "Unidade",
                "image": image_string
            },{
                "_id": ANY,
                "description": "IMA BORBOLETA C/04 A1",
                "brand": "Ima brand",
                "reference": "16",
                "amount": 0,
                "location": "",
                "last_change": "+4  23/09/2025 17:06:12",
                "stock": 4,
                "measure": "Unidade",
                "image": image_string
            }]
        }
    }

    data = {
        "params": params,
        "get_product_by_code": get_product_by_code,
        "expected_response": expected_response
    }

    return data


def get_product_not_found_data():

    params = {
        "code": "16"
    }

    data = {
        "params": params
    }

    return data


def get_product_product_without_image_data():

    params = {
        "code": "16"
    }

    get_product_by_code = {
        "_id": ObjectId("64a7f3f5f1c2e3b1a5d6e7f8"),
        "variants":[{
            "_id": ObjectId(),
            "code": "16",
            "description": "IMA BORBOLETA C/04",
            "brand": "MAX PING",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": "imagem_bytes"
        },{
            "_id": ObjectId(),
            "code": "16",
            "description": "IMA BORBOLETA C/04 A1",
            "brand": "Ima brand",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": "imagem_bytes"
        }]
    }

    expected_body = {
        "data":{
            "operation": "Get",
            "count": 2,
            "attributes": [{
                "_id": ANY,
                "code": "16",
                "description": "IMA BORBOLETA C/04",
                "brand": "MAX PING",
                "reference": "16",
                "amount": 0,
                "location": "",
                "last_change": "+4  23/09/2025 17:06:12",
                "stock": 4,
                "measure": "Unidade",
                "image": f"https://localhost:{PORT}/erro.jpg"
            },{
                "_id": ANY,
                "code": "16",
                "description": "IMA BORBOLETA C/04 A1",
                "brand": "Ima brand",
                "reference": "16",
                "amount": 0,
                "location": "",
                "last_change": "+4  23/09/2025 17:06:12",
                "stock": 4,
                "measure": "Unidade",
                "image": f"https://localhost:{PORT}/static/erro.jpg"
            }]
        }
    }
    data = {
        "params": params,
        "get_product_by_code": get_product_by_code,
        "expected_body": expected_body
    }

    return data


def get_product_with_int_code_data():

    params = {
        "code": 16 #Must be string
    }

    data = {
        "params": params
    }

    return data