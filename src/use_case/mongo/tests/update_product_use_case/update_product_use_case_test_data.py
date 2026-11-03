import os

from bson import ObjectId, Binary

from datetime import datetime

from unittest.mock import ANY

from src.utils.image_type import image_string_splitted

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

def update_product_sucessfully_data():

    get_variant_by_code_and_id = {
       '_id': ObjectId('6ae2346bbac0f284def2e7f9'), 
       'description': 'Product A', 
       'stock': 10, 
       'image': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\nIDAT\x08\xd7c`\x00\x00\x00\x02\x00\x01\xe2&\x05\x9b\x00\x00\x00\x00IEND\xaeB`\x82', 
       'brand': 'Kit-Kat', 
       'reference': 'Kit1030', 
       'last_change': datetime(2026, 10, 28, 14, 44, 11, 140000), 
       'location': 'A10', 
       'measure': 'Unidade', 
       'keepBuying': True,
       'warehouse':{
           "quantity_change": 10,
           "stock": 10,
           "measure": "Unidade",
           "last_change": datetime.now()
       }
    }

    body = {
        'description': 'Update Product A', 
        'stock': 0, 
        'brand': 'Lacta', 
        'image': image_string_splitted,
        'reference': 'Lacta22', 
        'location': 'A10', 
        'measure': 'Unidade', 
        'keepBuying': False,
    }

    params = {
        "code": "10",
        "_id": ObjectId("6ae2346bbac0f284def2e7f9")
    }

    entity_update = {
        **body,
        "last_change": datetime.now()
    }

    expect_response = {
        'data': {
            'operation': 'Update', 
            'count': 1, 
            'attributes': {
                'description': 'Update Product A', 
                'stock': 0, 
                'brand': 'Lacta', 
                'reference': 'Lacta22', 
                'location': 'A10', 
                'measure': 'Unidade', 
                'keepBuying': False, 
                '_id': ObjectId('6ae2346bbac0f284def2e7f9')}
        }}

    assert_called_product_repository_update = {
        'variants.$.description': 'Update Product A', 
        'variants.$.stock': 0, 
        'variants.$.brand': 'Lacta', 
        'variants.$.image': Binary(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\nIDAT\x08\xd7c`\x00\x00\x00\x02\x00\x01\xe2&\x05\x9b\x00\x00\x00\x00IEND\xaeB`\x82', 0), 'variants.$.reference': 'Lacta22', 
        'variants.$.keepBuying': False, 
        'variants.$.last_change': ANY}

    return {
        "get_variant_by_code_and_id": get_variant_by_code_and_id,
        "body": body,
        "params": params,
        "entity_update": entity_update,
        "expect_response": expect_response,
        "assert_called_product_repository_update":assert_called_product_repository_update
    }



def missing_required_fields_for_body_return_HttpUnprocessableEntity_data():

    params = {
        "code": "10",
        "_id": "" #must be not empty 
    }

    body = {
            'description': "New Product A"
    }

    data = {
        "params": params,
        "body": body
    }

    return data


def product_not_in_database_return_HttpNotFound_data():

    params = {
        "code": "10",
        "_id": "6953c87972d481a4b87b65d3" 
    }

    body = {
        'description': "New Product A" ,
    }

    data = {
        "params": params,
        "body": body
    }

    return data


def database_unavailable_return_HttpUnavailableService_data():

    params = {
        "code": "10",
        "_id": "6953c87972d481a4b87b65d3" 
    }

    body = {
        'description': "New Product A" ,
    }

    body_to_update = {
        'variants.$.code': '10',
        'variants.$.description': 'New Product A',
        'variants.$.last_change': ANY
        
        }

    data = {
        "params": params,
        "body": body,
        "body_to_update": body_to_update
    }

    return data


def update_product_raise_HttpInternalServerError_data():

    params = {
        "code": "10",
        "_id": "6953c87972d481a4b87b65d3" 
    }

    body = {
        'description': "New Product A" ,
    }

    body_to_update = {
        'variants.$.code': '10',
        'variants.$.description': 'New Product A',
        'variants.$.last_change': ANY
        }

    data = {
        "params": params,
        "body": body,
        "body_to_update": body_to_update
    }

    return data
