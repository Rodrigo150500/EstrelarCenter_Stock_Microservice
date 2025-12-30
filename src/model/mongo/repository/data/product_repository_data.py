from datetime import datetime

from bson.objectid import ObjectId

imagem_bytes = bytes([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
    0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
    0xDE, 0x00, 0x00, 0x00, 0x0A, 0x49, 0x44, 0x41,
    0x54, 0x08, 0xD7, 0x63, 0x60, 0x00, 0x00, 0x00,
    0x02, 0x00, 0x01, 0xE2, 0x26, 0x05, 0x9B, 0x00,
    0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE,
    0x42, 0x60, 0x82
  ])


def insert_product_data():

    fields = {
            "code": "10",
            "variants":[{
                "_id": ObjectId(),
                "description": "Product A",
                "stock": 10,
                "image": imagem_bytes,
                "brand": "Kit-Kat",
                "reference": "Kit1030",
                "last_change": datetime.now(),
                "location": "A10",
                "measure": "Unidade",
                "keepBuying": True
            },{
                "_id": ObjectId(),
                "description": "Product B",
                "stock": 15,
                "image": imagem_bytes,
                "brand": "Bis",
                "reference": "Bis1515",
                "last_change": datetime.now(),
                "location": "CX20",
                "measure": "Caixa",
                "keepBuying": False
            }]
            }
    
    insert_one = {
        "inserted_id": ObjectId(),
        "acknowledged": True
    }

    data = {
        "fields": fields,
        "insert_one": insert_one
    }

    return data


def insert_new_variant_in_product_exist_data():

    fields = {
        "description": "New Product B",
        "stock": 50,
        "brand": "Diamante Negro",
    }

    update_one = {
        "acknowledged": True,
        "matched_count": 1,
        "modified_count": 1
    }

    data = {
        "fields": fields,
        "update_one": update_one
    }

    return data


def get_product_by_code_return_product_data():

    find_one = {
            "code": "10",
            "variants":[{
                "_id": ObjectId(),
                "description": "Product A",
                "stock": 10,
                "image": imagem_bytes,
                "brand": "Kit-Kat",
                "reference": "Kit1030",
                "last_change": datetime.now(),
                "location": "A10",
                "measure": "Unidade",
                "keepBuying": True
            },{
                "_id": ObjectId(),
                "description": "Product B",
                "stock": 15,
                "image": imagem_bytes,
                "brand": "Bis",
                "reference": "Bis1515",
                "last_change": datetime.now(),
                "location": "CX20",
                "measure": "Caixa",
                "keepBuying": False
            }]
            }
    
    data = {
        "find_one": find_one
    }

    return data


def update_product_variant_data():

    fields = {
            "variants.$.description": "New Product D",
            "variants.$.stock": 88,
            "variants.$.last_change": datetime.now(),
            "variants.$.keepBuying": False
    }

    update_one = {
        "acknowledged": True,
        "matched_count": 1,
        "modified_count": 1
    }

    data = {
        "fields": fields,
        "update_one": update_one
    }

    return data


def get_all_products_data():
    
    find_one = [{
            "code": "10",
            "variants":[{
                "_id": ObjectId(),
                "description": "Product A",
                "stock": 10,
                "image": imagem_bytes,
                "brand": "Kit-Kat",
                "reference": "Kit1030",
                "last_change": datetime.now(),
                "location": "A10",
                "measure": "Unidade",
                "keepBuying": True
            },{
                "_id": ObjectId(),
                "description": "Product B",
                "stock": 15,
                "image": imagem_bytes,
                "brand": "Bis",
                "reference": "Bis1515",
                "last_change": datetime.now(),
                "location": "CX20",
                "measure": "Caixa",
                "keepBuying": False
            }]
            }]
    
    data = {
        "find_one": find_one
    }

    return data

def remove_item_data():

    update_one = {
        "acknowledged": True,
        "matched_count": 1,
        "modified_count": 1
    }

    data = {
        "update_one": update_one
    }

    return data


def remove_product_data():
    
    delete_one = {
        "acknowledged":True,
        "deleted_count":1
    }

    data = {
        "delete_one": delete_one
    }

    return data


def check_if_variant_exists_data():

    find_one = {
        "_id": "6953c87972d481a4b87b65d3"
    }

    

    data = {
        "find_one": find_one
    }

    return data
