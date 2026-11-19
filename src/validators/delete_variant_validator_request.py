from bson import ObjectId
from cerberus import Validator

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def delete_variant_validator_request(params: dict):

  def validate_object_id(field, value, error):
      if not ObjectId.is_valid(value):
          error(field, "Variant ID is invalid")

  params_validator = Validator({
      "code": {
          "type": "string",
          "required": True,
          "empty": False
      },
      "_id": {
          "type": "string",
          "required": True,
          "empty": False,
          "check_with": validate_object_id
      }
  })

  response = params_validator.validate(params)

  if response is False:
      raise HttpUnprocessableEntity(
          message=params_validator.errors
      )