

def remove_item_succesfully_data(): 

    params = {
        "code": "10",
        "_id": "68b70ef826423e500863c1c7"}

    expected_response = {
        "data":{
            "operation": "Update",
            "count": 1,
            "attributes": params
        }
    }

    data = {
        "params": params,
        "expected_response": expected_response 
    }

    return data


def remove_item_that_not_exists_data():
    
    params = {
        "code": "10",
        "_id": "68b70ef826423e500863c1c7"
        }
    
    data = {
        "params": params
    }

    return data