from unittest.mock import ANY

from bson.objectid import ObjectId

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from src.utils.image_type import image_string, image_string_splitted

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
        "keepBuying": True,
        "quantity_change": 4
    }


    body_response = {
        "_id": ANY,
        "code": "10",
        "variants":[{
            "_id": ANY,
            "description": "Chocolate kit-kat 41g",
            "stock": 15,
            "brand": "kit-kat",
            "reference": "kit-154",
            "location": "CX15",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": ANY,
            "quantity_change": 4
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
        "keepBuying": True,
        "quantity_change": 3
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
            "quantity_change": 3
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
            'reference': "KIT104",
            "quantity_change": 3

        }]
    }

   
    data = {
        "body": body,
        "get_product_by_code": get_product_by_code
    }

    return data


def error_unavailable_service_database_data():

    body = {
        "code": "10",
        "description": "Chocolate kit-kat 41g",
        "stock": 15,
        "image": image_string,
        "brand": "kit-kat",
        "reference": "kit-154",
        "location": "CX15",
        "measure": "Caixa",
        "keepBuying": True,
        "quantity_change": 4
    }

    data = {
        "body": body
    }

    return data