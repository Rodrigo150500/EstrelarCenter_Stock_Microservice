from unittest.mock import ANY

from src.utils.image_type import image_string


def update_product_sucessfully_data():

    params = {
        "code": "10",
        "_id": "6953c87972d481a4b87b65d3" 
    }

    body = {
            "code": "10",
            'description': "New Product A" ,
            'measure': "Unidade",
            'stock': 25,
            'brand': "Kit-Kat",
            'image': image_string,
            'location': "P9",
            'reference': "KIT104",
            "quantity_change": 3
    }

    expected_response = {
        "data":{
            "operation": "Update",
            "count": 1
        }
    }

    body_to_update = {
        'variants.$.code': '10',
        'variants.$.description': 'New Product A',
        'variants.$.measure': 'Unidade',
        'variants.$.stock': 25,
        'variants.$.brand': 'Kit-Kat',
        'variants.$.image': 'https://localhost:6000/static/stock/src/assets/erro.jpg',
        'variants.$.location': 'P9',
        'variants.$.reference': 'KIT104',
        'variants.$.quantity_change': 3,
        'variants.$.last_change': ANY
        }
    

    data = {
        "params": params,
        "body": body,
        "expected_response": expected_response,
        "body_to_update": body_to_update
    }

    return data


def missing_required_fields_for_body_return_HttpUnprocessableEntity_data():

    params = {
        "code": "10",
        "_id": "" #must be not empty 
    }

    body = {
            # "code": "10", Must be in request
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
        "code": "10",
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
        "code": "10",
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
        "code": "10",
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
