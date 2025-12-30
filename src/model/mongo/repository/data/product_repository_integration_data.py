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


def insert_product_variant_data():

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

    return fields


def insert_new_variant_in_product_exist_data():
    
    fields = {
                "_id": ObjectId(),
                "variantId": 3,
                "description": "Product C",
                "stock": 25,
                "image": imagem_bytes,
                "brand": "Diamante Negro",
                "reference": "Diamant44",
                "last_change": datetime.now(),
                "location": "CX18",
                "measure": "Unidade",
                "keepBuying": True
            }
    
    return fields


def update_product_variant_data():
     
    fields = {
            "variants.$.description": "New Product D",
            "variants.$.stock": 88,
            "variants.$.last_change": datetime.now(),
            "variants.$.keepBuying": False
            }

    return fields


def check_if_product_exists_data():

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
    
    data = {
         "fields": fields
    }

    return data