import os
from src.model.firebase.repository.interface.product_repository_interface import ProductRepositoryFirebaseInterface

COLLECTION_NAME = os.getenv("COLLECTION_NAME_FIREBASE_PRODUCTS")

class ProductRepositoryFirebase(ProductRepositoryFirebaseInterface):

  def __init__(self, connection):

    self.__connection = connection
    self.__reference = COLLECTION_NAME


  def get_product_by_code(self, code: str):

    product = self.__connection.reference(f"{self.__reference}/{code}").get()

    return product
  
  
  def insert_or_update_product(self, code: str, fields: dict) -> bool:

    try:

      self.__connection.reference(f"{self.__reference}/{code}").update(
        fields
      )

      return True
    
    except Exception:

      return False

  
  def delete_product_by_code(self, code: str):

    try:

      self.__connection.reference(f"{self.__reference}/{code}").delete()

      return True

    except Exception as exception:

      return False
  