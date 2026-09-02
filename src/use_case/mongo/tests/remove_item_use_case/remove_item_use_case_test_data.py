

def remove_item_succesfully_data(): 

    params = {
        "code": "10",
        "_id": "68b70ef826423e500863c1c7"}

    data = {
        "params": params
    }

    return data

def delete_product_with_one_variant_data():

    params = {
        "code": "10",
        "_id": "68b70ef826423e500863c1c7"

    }

    exists = True
    get_variant_count = 1


    return {
        "exists": exists,
        "get_variant_count": get_variant_count,
        "params": params
    }



def remove_item_that_not_exists_data():
    
    params = {
        "code": "10",
        "_id": "68b70ef826423e500863c1c7"
        }
    
    data = {
        "params": params
    }

    return data