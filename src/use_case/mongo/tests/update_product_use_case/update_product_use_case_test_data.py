import os

from bson import ObjectId, Binary

from datetime import datetime

from unittest.mock import ANY

from src.utils.image_type import image_string_splitted

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

def valid_setup():

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

    return get_variant_by_code_and_id, body, params, entity_update, expect_response, assert_called_product_repository_update
    


def update_without_image_successfully_data():

    get_variant_by_code_and_id, body, params, entity_update, expect_response, assert_called_product_repository_update = valid_setup()

    del body["image"]
    del entity_update["image"]
    del assert_called_product_repository_update["variants.$.image"]

    return get_variant_by_code_and_id, body, params, entity_update, expect_response, assert_called_product_repository_update


def update_with_warehouse_successfully_data():

    get_variant_by_code_and_id, body, params, entity_update, expect_response, assert_called_product_repository_update = valid_setup()

    body["warehouse"] = {
        "quantity_change": 0,
        "stock": 0,
        "measure": "Caixa",
    }

    entity_update["warehouse"] = {
        **body["warehouse"],
        "last_change": datetime.now()
    }

    
    expect_response["data"]["attributes"]["warehouse"] = {**body['warehouse']}

    assert_called_product_repository_update["variants.$.warehouse"] = {
            **body["warehouse"],
            "last_change": ANY
    }

    return  get_variant_by_code_and_id, body, params, entity_update, expect_response, assert_called_product_repository_update


def nothing_to_update_successfully_data():

    get_variant_by_code_and_id, _, params, _, expect_response, assert_called_product_repository_update = valid_setup()

    body = {
            'description': 'Product A', 
            'stock': 10, 
            'brand': 'Kit-Kat',  
            'reference': 'Kit1030', 
            'location': 'A10', 
            'measure': 'Unidade', 
            'keepBuying': True,
            'warehouse':{
                "quantity_change": 10,
                "stock": 10,
                "measure": "Unidade",
            }
    }

    entity_update = {
        **body,
        "last_change": datetime.now()
    }

    entity_update['warehouse']['last_change'] = datetime.now()

    return get_variant_by_code_and_id, body, params, entity_update, expect_response, assert_called_product_repository_update 