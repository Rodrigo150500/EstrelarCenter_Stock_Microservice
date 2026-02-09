from datetime import datetime

from bson.objectid import ObjectId

from src.utils.image_type import imagem_bytes

from unittest.mock import ANY


def setup_use_case_data():
    
    product = {
    "code": "10",
    "variants": [
        {
            "_id": ObjectId(),
            "description": "Product A",
            "stock": 10,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-100",
            "location": "CX01",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 1
        },
        {
            "_id": ObjectId(),
            "description": "Product B",
            "stock": 12,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-101",
            "location": "CX02",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -2
        },
        {
            "_id": ObjectId(),
            "description": "Product C",
            "stock": 15,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-102",
            "location": "CX03",
            "measure": "Caixa",
            "keepBuying": False,
            "last_change": datetime.now(),
            "quantity_change": 3
        },
        {
            "_id": ObjectId(),
            "description": "Product D",
            "stock": 18,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-103",
            "location": "CX04",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -1
        },
        {
            "_id": ObjectId(),
            "description": "Product E",
            "stock": 20,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-104",
            "location": "CX05",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 4
        },
        {
            "_id": ObjectId(),
            "description": "Product F",
            "stock": 22,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-105",
            "location": "CX06",
            "measure": "Unidade",
            "keepBuying": False,
            "last_change": datetime.now(),
            "quantity_change": -3
        },
        {
            "_id": ObjectId(),
            "description": "Product G",
            "stock": 25,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-106",
            "location": "CX07",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 2
        },
        {
            "_id": ObjectId(),
            "description": "Product H",
            "stock": 27,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-107",
            "location": "CX08",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -4
        },
        {
            "_id": ObjectId(),
            "description": "Product I",
            "stock": 30,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-108",
            "location": "CX09",
            "measure": "Caixa",
            "keepBuying": False,
            "last_change": datetime.now(),
            "quantity_change": 5
        },
        {
            "_id": ObjectId(),
            "description": "Product J",
            "stock": 32,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-109",
            "location": "CX10",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -2
        },{
            "_id": ObjectId(),
            "description": "Product K",
            "stock": 35,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-110",
            "location": "CX11",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 3
        },
        {
            "_id": ObjectId(),
            "description": "Product L",
            "stock": 38,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-111",
            "location": "CX12",
            "measure": "Unidade",
            "keepBuying": False,
            "last_change": datetime.now(),
            "quantity_change": -2
        },
        {
            "_id": ObjectId(),
            "description": "Product M",
            "stock": 40,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-112",
            "location": "CX13",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 4
        },
        {
            "_id": ObjectId(),
            "description": "Product N",
            "stock": 42,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-113",
            "location": "CX14",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -3
        },
        {
            "_id": ObjectId(),
            "description": "Product O",
            "stock": 45,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-114",
            "location": "CX15",
            "measure": "Caixa",
            "keepBuying": False,
            "last_change": datetime.now(),
            "quantity_change": 5
        },
        {
            "_id": ObjectId(),
            "description": "Product P",
            "stock": 47,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-115",
            "location": "CX16",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -4
        },
        {
            "_id": ObjectId(),
            "description": "Product Q",
            "stock": 50,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-116",
            "location": "CX17",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 6
        },
        {
            "_id": ObjectId(),
            "description": "Product R",
            "stock": 52,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-117",
            "location": "CX18",
            "measure": "Unidade",
            "keepBuying": False,
            "last_change": datetime.now(),
            "quantity_change": -5
        },
        {
            "_id": ObjectId(),
            "description": "Product S",
            "stock": 55,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-118",
            "location": "CX19",
            "measure": "Caixa",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": 7
        },
        {
            "_id": ObjectId(),
            "description": "Product T",
            "stock": 57,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-119",
            "location": "CX20",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -6
        },
        {
            "_id": ObjectId(),
            "description": "Product U",
            "stock": 60,
            "image": imagem_bytes,
            "brand": "kit-kat",
            "reference": "REF-120",
            "location": "CX21",
            "measure": "Caixa",
            "keepBuying": False,
            "last_change": datetime.now(),
            "quantity_change": 8
        },
        {
            "_id": ObjectId(),
            "description": "Product V",
            "stock": 62,
            "image": imagem_bytes,
            "brand": "Bis",
            "reference": "REF-121",
            "location": "CX22",
            "measure": "Unidade",
            "keepBuying": True,
            "last_change": datetime.now(),
            "quantity_change": -7
        }

    ]
    }
    
    data = {
        "product": product
    }
    
    return data


def get_product_sucessfully_data(object_id_list: list):

    params = {
        "search": "REF-100",
        "fields": ["brand", "reference"],
        "last_id": ""
    }

    expected_response = {
        'data': {
            'operation': 'Get',
            'count': 1, 
            'attributes':[{
                '_id': object_id_list[0], 
                'description': 'Product A', 
                'stock': 10, 
                'image': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\nIDAT\x08\xd7c`\x00\x00\x00\x02\x00\x01\xe2&\x05\x9b\x00\x00\x00\x00IEND\xaeB`\x82', 
                'brand': 'kit-kat', 
                'reference': 'REF-100', 
                'location': 'CX01', 
                'measure': 'Caixa', 
                'keepBuying': True, 
                'last_change': ANY, 
                'quantity_change': 1}]
            }
            }

    data = {
        "params": params,
        "expected_response": expected_response
    }

    return data


def adding_last_id_should_return_second_part_data(object_id_list: list):

    params = {
        "search": "product",
        "fields": ["description", "reference"],
        "last_id": object_id_list[20]
    }

    expected_response = {
        "data":{
            "operation": "Get",
            "count": 1,
            "attributes":[{
                '_id': object_id_list[21], 
                'description': 'Product V', 
                'stock': 62, 
                'image': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\nIDAT\x08\xd7c`\x00\x00\x00\x02\x00\x01\xe2&\x05\x9b\x00\x00\x00\x00IEND\xaeB`\x82', 
                'brand': 'Bis', 
                'reference': 'REF-121', 
                'location': 'CX22', 
                'measure': 'Unidade', 
                'keepBuying': True, 
                'last_change':ANY, 
                'quantity_change': -7}]
        }
    }

    data = {
        "params": params,
        "expected_response": expected_response
    }

    return data


def product_not_found_should_return_error_data():
    
    params = {
        "search": "not found",
        "fields": ["description", "reference", "brand"],
        "last_id": ""
    }

    data = {
        "params": params
    }

    return data



