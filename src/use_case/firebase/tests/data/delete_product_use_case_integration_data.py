def delete_product_sucessfully_data():
    
    get_product_by_code = {
        "code": "123456",
        "description": "Test Product"
    }

    response_body = {
        "data":{
            "operation":"delete",
            "count": 1,
            "attributes": {
                "code": "123456"
            }
        }
    }

    data = {
        "get_product_by_code": get_product_by_code,
        "response_body": response_body
    }

    return data
    