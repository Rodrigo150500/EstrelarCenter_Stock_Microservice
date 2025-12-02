from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from cerberus import Validator

def get_image_product_validator_request(params: dict):

  params_validator = Validator({  
        "code":{"type": "string", "required":True},
        "item":{"type": "integer", "required": True}
            })

  response = params_validator(params)
  if response is False:
    raise HttpUnprocessableEntity(
      message=params_validator.errors,
      expected_data={
        "code":"123"
      }
    )
  