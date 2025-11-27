from pymongo.results import UpdateResult, DeleteResult

from bson.objectid import ObjectId


def get_product_by_code_data():

    find_one = {
        "_id": ObjectId("68b70ef826423e500863c1c6"),
        "10":[{
            "code": "10",
            "description": "Product A",
            "brand": "brand",
            "reference": "IMA",
            "location": "C06",
            "last_change": "-3 23/09/2025 17:17:27",
            "stock": 5,
            "measure":"Unidade"

        }]
    }

    return find_one


def remove_item_data():

    remove_item = UpdateResult({
        "n": 1,               # matched_count
        "nModified": 1,       # modified_count
        "upserted": None,     # upserted_id
        "ok": 1.0             # operação OK
    },
        acknowledged=True)

    return remove_item


def delete_product_by_code_data():

    delete_one = DeleteResult({'n': 1, 'ok': 1.0}, acknowledged=True)

    return delete_one   


def insert_product_item_data():

    fields = {
            "code": "10",
            "description": "Product A",
            "brand": "brand",
            "reference": "IMA",
            "location": "C06",
            "last_change": "-3 23/09/2025 17:17:27",
            "stock": 5,
            "measure":"Unidade"
            }
    
    update_one = UpdateResult({
        "n": 1,               # matched_count
        "nModified": 1,       # modified_count
        "upserted": None,     # upserted_id
        "ok": 1.0             # operação OK
    },
        acknowledged=True)


    data = {
        "fields": fields,
        "update_one": update_one
    }

    return data


def update_product_item_data():

    fields = {
            "code": "10",
            "description": "Product A",
            "brand": "brand",
            "reference": "IMA",
            "location": "C06",
            "last_change": "-3 23/09/2025 17:17:27",
            "stock": 5,
            "measure":"Unidade"
            }
    
    update_one = UpdateResult({
        "n": 1,               # matched_count
        "nModified": 1,       # modified_count
        "upserted": None,     # upserted_id
        "ok": 1.0             # operação OK
    },
        acknowledged=True)

   

    data = {
        "fields": fields,
        "update_one": update_one
    }

    return data


def get_all_products_data():

    find = [{
        "10":[{
            "code": "10",
            "description": "Product A",
            "brand": "brand",
            "reference": "IMA",
            "location": "C06",
            "last_change": "-3 23/09/2025 17:17:27",
            "stock": 5,
            "measure":"Unidade"
        }]
    }, {
        "11":[{
            "code": "11",
            "description": "Product B",
            "brand": "brand",
            "reference": "IMA",
            "location": "C06",
            "last_change": "-3 23/09/2025 17:17:27",
            "stock": 5,
            "measure":"Unidade"
        },{
            "code": "11",
            "description": "Product B1",
            "brand": "brand",
            "reference": "IMA",
            "location": "C06",
            "last_change": "-3 23/09/2025 17:17:27",
            "stock": 5,
            "measure":"Unidade"
        }]
    }]

    data = {
        "find": find
    }

    return data