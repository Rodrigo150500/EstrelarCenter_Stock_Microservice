import re

from datetime import datetime

from bson.objectid import ObjectId


def get_product_sucessfully_data():

    params = {
        "search": "product",
        "fields": ["description"],
        "last_id": ""
    }

    search_by_text=[{
        '_id': ObjectId(), 
        'description': 'Product V', 
        'stock': 62, 
        'image': b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\nIDAT\x08\xd7c`\x00\x00\x00\x02\x00\x01\xe2&\x05\x9b\x00\x00\x00\x00IEND\xaeB`\x82', 
        'brand': 'Bis', 
        'reference': 'REF-121', 
        'location': 'CX22', 
        'measure': 'Unidade', 
        'keepBuying': True, 
        'last_change': datetime.now(), 
        'quantity_change': -7
        }]
    
    expected_response = {
        "data":{
            "operation": "Get",
            "count": 1,
            "attributes": search_by_text
        }
    }

    pipeline = [
        {"$unwind":"$variants"},
        {"$match":{"$or": [{"variants.description": {"$regex": re.escape(params["search"]), "$options": "i"}}]}},
        {"$sort":{"variants._id":1}},
        {"$limit": 10},
        {"$replaceRoot":{"newRoot":"$variants"}}]

    data = {
        "params": params,
        "search_by_text": search_by_text,
        "pipeline": pipeline,
        "expected_response": expected_response
    }

    return data


def product_not_in_db_return_not_found_data():

    params = {
        "search": "product",
        "fields": ["description"],
        "last_id": ""
    }

    data = {
        "params": params
    }

    return data


def error_in_database_return_database_unavailable_data():

    params = {
        "search": "product",
        "fields": ["description"],
        "last_id": ""
    }

    data = {
        "params": params
    }

    return data


def schema_params_should_return_unprocessable_entity_data():

    params = {
        "search": "",
        "fields": ["marca"],
        "last_id": ""
    }

    data = {
        "params": params
    }

    return data
