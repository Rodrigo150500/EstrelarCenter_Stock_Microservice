from bson.objectid import ObjectId
from bson.errors import InvalidId

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from cerberus import Validator

def remove_item_validator_request(params: dict):

  params_validator = Validator({  
        "code":{"type": "string", "required":True},
        "_id":{"type": "string", "required": True}    
  })

  try:

    ObjectId(params["_id"])
  
  except (InvalidId) as exception:

    print(f"Error:[RemoveItemValidatorRequest][_id]: {str(exception)}")
    
    raise HttpUnprocessableEntity(f"Error: {str(exception)}")

  response = params_validator(params)

  if response is False:

    error = params_validator.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]

    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    print(f"Error:[RemoveItemValidatorRequest][Params]: {formatted_error_message}")

    raise HttpUnprocessableEntity(
      message=params_validator.errors
    )