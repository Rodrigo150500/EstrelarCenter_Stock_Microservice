import os
from src.model.firebase.repository.interface.product_repository_interface import ProductRepositoryFirebaseInterface
from src.errors.types.http_unavailable_service import HttpUnavailableService

COLLECTION_NAME = os.getenv("COLLECTION_NAME_FIREBASE_PRODUCTS")

class ProductRepositoryFirebase(ProductRepositoryFirebaseInterface):

  def __init__(self, connection):

    self.__connection = connection
    self.__reference = COLLECTION_NAME


  def get_product_by_code(self, code: str) -> dict:

    try:

      product = self.__connection.reference(f"{self.__reference}/{code}").get()

      return product
    
    except Exception as exception:

      print(f"Error:[product_repository_firebase][get_product_by_code]: {str(exception)}")


      raise HttpUnavailableService("Banco de dados indisponível")
  
  
  def insert_or_update_product(self, code: str, fields: dict) -> bool:

    try:

      self.__connection.reference(f"{self.__reference}/{code}").update(
        fields
      )

      return True
    
    except Exception as exception:

      print(f"Error:[product_repository_firebase][insert_or_update_product]: {str(exception)}")

      raise HttpUnavailableService("Banco de dados indisponível")

  
  def delete_product_by_code(self, code: str) -> bool:

    try:

      self.__connection.reference(f"{self.__reference}/{code}").delete()

      return True

    except Exception as exception:

      print(f"Error:[product_repository_firebase][delete_product_by_code]: {str(exception)}")

      raise HttpUnavailableService("Banco de dados indisponível")

  