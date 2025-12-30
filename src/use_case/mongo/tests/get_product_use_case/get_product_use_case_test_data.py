import os
from bson.objectid import ObjectId

from src.utils.image_type import imagem_bytes

PORT = os.getenv("PORT")

def get_product_sucessfully():

    params = {
        "code": "16"
    }

    get_product_by_code = {
        "_id": ObjectId("64a7f3f5f1c2e3b1a5d6e7f8"),
        "code": "16",
        "variants":[{
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
    
    expected_body_response = {
        "data":{
            "operation": "Get",
            "count": 2,
            "attributes": get_product_by_code
        }
    }
    {
        'data': {
            'operation': 'Get',
            'count': 2,
            'attributes': [{
                'description': 'IMA BORBOLETA C/04', 
                'brand': 'MAX PING', 
                'reference': '16', 
                'amount': 0, 
                'location': '', 'last_change': '+4  23/09/2025 17:06:12', 'stock': 4, 'measure': 'Unidade', 'image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACklEQVQI12NgAAAAAgAB4iYFmwAAAABJRU5ErkJggg=='}, {'description': 'IMA BORBOLETA C/04 A1', 'brand': 'Ima brand', 'reference': '16', 'amount': 0, 'location': '', 'last_change': '+4  23/09/2025 17:06:12', 'stock': 4, 'measure': 'Unidade', 'image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACklEQVQI12NgAAAAAgAB4iYFmwAAAABJRU5ErkJggg=='}]}
        }
    data = {
        "params": params,
        "get_product_by_code": get_product_by_code,
        "expected_body_response": expected_body_response
    }

    return data


def get_product_not_found():

    params = {
        "code": "16"
    }

    data = {
        "params": params
    }

    return data


def get_product_product_without_image():

    params = {
        "code": "16"
    }

    get_product_by_code = {
        "_id": ObjectId("64a7f3f5f1c2e3b1a5d6e7f8"),
        "16":[{
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
            "operation": "get",
            "count": 2,
            "attributes": [{
                "code": "16",
                "description": "IMA BORBOLETA C/04",
                "brand": "MAX PING",
                "reference": "16",
                "amount": 0,
                "location": "",
                "last_change": "+4  23/09/2025 17:06:12",
                "stock": 4,
                "measure": "Unidade",
                "image": f"https://localhost:{PORT}/static/stock/src/assets/erro.jpg"
            },{
                "code": "16",
                "description": "IMA BORBOLETA C/04 A1",
                "brand": "Ima brand",
                "reference": "16",
                "amount": 0,
                "location": "",
                "last_change": "+4  23/09/2025 17:06:12",
                "stock": 4,
                "measure": "Unidade",
                "image": f"https://localhost:{PORT}/static/stock/src/assets/erro.jpg"
            }]
        }
    }
    data = {
        "params": params,
        "get_product_by_code": get_product_by_code,
        "expected_body": expected_body
    }

    return data


def get_product_with_int_code():

    params = {
        "code": 16
    }

    data = {
        "params": params
    }

    return data