from unittest.mock import ANY

from bson.objectid import ObjectId

from src.utils.export_image_binary_to_string64 import export_image_binary_to_string64
from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from datetime import datetime

imagem_bytes = bytes([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
    0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
    0xDE, 0x00, 0x00, 0x00, 0x0A, 0x49, 0x44, 0x41,
    0x54, 0x08, 0xD7, 0x63, 0x60, 0x00, 0x00, 0x00,
    0x02, 0x00, 0x01, 0xE2, 0x26, 0x05, 0x9B, 0x00,
    0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE,
    0x42, 0x60, 0x82
])

image_string = "'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACklEQVQI12NgAAAAAgAB4iYFmwAAAABJRU5ErkJggg=='"


def insert_product_sucessfully():
    
    body = {
        "code": "10",
        "description": "Chocolate kit-kat 41g",
        "stock": 15,
        "image": image_string,
        "brand": "kit-kat",
        "reference": "kit-154",
        "location": "CX15",
        "measure": "Caixa",
        "keepBuying": True
    }


    body_response = {
        "code": "10",
        "variants":[{
            "description": "Chocolate kit-kat 41g",
            "stock": 15,
            "image": export_image_string64_to_binary(image_string),
            "brand": "kit-kat",
            "reference": "kit-154",
            "location": "CX15",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": ANY
        }]
    }

    expected_body = {
        "data":{
            "operation": "Insert",
            "count": 1,
            "attributes": body_response
        }
    }

    data = {
        "body": body,
        "expected_body": expected_body
    }

    return data


def insert_product_with_int_code():

    body = {
        "code": 10, #Wrong type
        "description": "Chocolate kit-kat 41g",
        "stock": 15,
        "image": image_string,
        "brand": "kit-kat",
        "reference": "kit-154",
        "location": "CX15",
        "measure": "Caixa",
        "keepBuying": True
    }

    data = {
        "body": body
    }

    return data


def insert_product_that_already_exists():
    
    body = {
            'code': "16",
            'description': "Product A" ,
            'measure': "Unidade",
            'stock': 25,
            'brand': "Kit-Kat",
            'image': "imagem_bytes",
            'location': "P9",
            'reference': "KIT104",
            "keepBuying": True,
    }

    get_product_by_code = {
        "_id": ObjectId("64a7f3f5f1c2e3b1a5d6e7f8"),
        'code': "16",
        'variantes':[{
            'description': "Product A" ,
            'measure': "Unidade",
            'stock': 25,
            'brand': "Kit-Kat",
            'last_change': ANY  ,
            'image': "imagem_bytes",
            'location': "P9",
            'reference': "KIT104"
        }]
    }

   
    data = {
        "body": body,
        "get_product_by_code": get_product_by_code
    }

    return data