from bson.objectid import ObjectId
from bson.errors import InvalidId


from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from cerberus import Validator


def update_product_validator_request(body: dict, params: dict):

  params_validate = Validator({
    "code": {"type": "string", "required": True, "empty": False},
    "_id": {"type": "string", "required": True, "minlength": 1}
  })

  body_validate = Validator({         
            "description": {"type": "string", "required": False, "empty": False},
            "brand": {"type": "string", "required": False, "empty": False},
            "reference": {"type": "string", "required": False, "empty": False},
            "location": {"type": "list", "required": False, "empty": False},
            "image": {"type": "string", "required": False, "empty": False},
            "measure": {"type": "string", "required": False, "allowed": ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"], "empty": False},
            "quantity_change":{"type": "integer", "required": False, "empty": False, "dependencies": "stock"},
            "stock": {"type": "integer", "required": False, "min": 0, "empty": False, "dependencies": "quantity_change"},
            "keepBuying": {"type": "boolean", "required": False},
            "warehouse": {
              "type": "dict",
              "required": False,
              "schema":{
                "quantity_change": {"type": "integer", "required": False, 'empty': False, "dependencies": ["^warehouse", "stock"]},
                "stock": {"type": "integer", "required": False, "min": 0, "dependencies": ["^warehouse", "stock"], "empty": False},
                "measure": {"type": "string", "required": False, "allowed": ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"], "dependencies": "^warehouse", "empty": False},
                "location": {"type": "list", "required": False, "dependencies": "^warehouse", "empty": False}
              }
            }    
  })

  try:

    ObjectId(params["_id"])
  
  except (InvalidId) as exception:
    
    raise HttpUnprocessableEntity(f"Error: {str(exception)}")

  response_body = body_validate.validate(body)
  response_params = params_validate.validate(params)

  if response_body is False:

    error = body_validate.errors
    raise HttpUnprocessableEntity(
      message=error
    )
  
  if response_params is False:

    error = params_validate.errors

    raise HttpUnprocessableEntity(
      message=error
    )
  


