from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from cerberus import Validator

def get_product_validator_request(params: dict):
  
  params_validator = Validator({  
        "code":{"type": "string", "required":True, "minlength": 1}
            })

  response = params_validator(params)
  
  if response is False:

    error = params_validator.errors

    raise HttpUnprocessableEntity(
      message=error
    )
  