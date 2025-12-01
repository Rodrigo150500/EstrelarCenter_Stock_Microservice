def delete_product_use_case_sucessfully_data():

    expected_response = {
        "data":{
            "operation":"delete",
            "count": 1,
            "attributes": {
                "code": "16"
            }
        }
    }

    data = {
        "expected_response": expected_response
    }

    return data