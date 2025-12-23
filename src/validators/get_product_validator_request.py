from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from cerberus import Validator

def get_product_validator_request(params: dict):
  
  body_validator = Validator({  
        "code":{"type": "string", "required":True, "minlength": 1}
            })

  response = body_validator(params)
  
  if response is False:
    raise HttpUnprocessableEntity(
      message=body_validator.errors
    )
  