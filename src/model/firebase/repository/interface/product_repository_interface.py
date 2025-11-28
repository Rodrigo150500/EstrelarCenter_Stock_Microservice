from abc import ABC, abstractmethod

class ProductRepositoryFirebaseInterface(ABC):

  @abstractmethod
  def get_product_by_code(self, code: str):
    pass
  
  @abstractmethod
  def insert_or_update_product(self, code: str, fields: dict):
    pass
  
  @abstractmethod
  def delete_product_by_code(self, code: str):
    pass