from datetime import datetime
from bson.objectid import ObjectId

class ProductEntity:

    def __init__(self, code, description, image, keepBuying, measure, quantity_change, stock, _id = None, brand = None, last_change = None, warehouse = None, location = None, reference = None ):

        self._id = _id
        self.code = code
        self.brand = brand
        self.description = description
        self.image = image
        self.keepBuying = keepBuying
        self.last_change = last_change
        self.location = location
        self.measure = measure
        self.quantity_change = quantity_change
        self.reference = reference
        self.stock = stock
        self.warehouse = warehouse

    @classmethod
    def create(cls, data):


        if


    
        return cls(
            code = data["code"],
            description = data["description"],
            image = data["image"],
            keepBuying = data["keepBuying"],
            measure = data["measure"],
            quantity_change = data["quantity_change"],
            stock = data["stock"],
            _id = ObjectId(),
            last_change = datetime.now(),
            warehouse = data.get("warehouse"),
            location = data.get("location"),
            reference = data.get("reference")
        )
        
         

    def restore():
        pass

    def udpate():
        pass