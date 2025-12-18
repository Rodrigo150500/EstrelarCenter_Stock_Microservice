from unittest.mock import ANY

from src.utils.export_image_string64_to_binary import export_image_string64_to_binary

from src.utils.image_type import image_string

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
        "_id": ANY,
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


def insert_product_that_already_exists():

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

   
    data = {
        "body": body,
    }

    return data


