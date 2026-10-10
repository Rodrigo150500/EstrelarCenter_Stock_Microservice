from datetime import datetime

from bson.objectid import ObjectId

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

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

        required_fields = ["code", "description", "image", "measure", "quantity_change", "stock", "keepBuying"]
        warehouse_required_fields = ["quantity_change", "stock", "measure"]

        measure_allowed = ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"]

        #Produto validação
        #Verificação de campos obrigatórios
        for field in required_fields:
            if field not in data:    
                raise HttpUnprocessableEntity(message=f"Campo obrigatório: [{field}] não encontrado")

            if data[field] == "":
                raise HttpUnprocessableEntity(message=f"O campo {field} não pode estar vazio")


        if data["measure"] not in measure_allowed:
            raise HttpUnprocessableEntity(message=f"O campo Medida deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote")
            

        if data["stock"] < 0:
            raise HttpUnprocessableEntity(message=f"O campo Estoque não pode ser negativo")


        #Warehouse validação
        #Verificação de campos obrigatórios em warehouse
        if "warehouse" in data:
            for field in warehouse_required_fields:
                if field not in data["warehouse"]:
                    raise HttpUnprocessableEntity(message=f"Campo obrigatório: [{field}] não encontrado")
                
                if data[field] == "":
                    raise HttpUnprocessableEntity(message=f"O campo {field} não pode estar vazio")
            
            if data["warehouse"]["stock"] < 0:
                raise HttpUnprocessableEntity(message=f"O campo Estoque não pode ser negativo")

            if data["warehouse"]["measure"] not in measure_allowed:
                        raise HttpUnprocessableEntity(message=f"O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote")


        return cls(
            _id = ObjectId(),
            code = data["code"],
            description = data["description"],
            image = data["image"],
            keepBuying = data["keepBuying"],
            measure = data["measure"],
            quantity_change = data["quantity_change"],
            stock = data["stock"],
            last_change = datetime.now(),
            warehouse = data.get("warehouse"),
            location = data.get("location"),
            reference = data.get("reference")
        )
        
         
    @classmethod
    def restore_variant(cls, code, data):
        return cls(
            _id = data["_id"],
            code = code,
            description = data["description"],
            brand = data.get("brand"),
            reference = data.get("reference"),
            location = data.get("location"),
            image = data["image"],
            measure = data["measure"],
            quantity_change = data["quantity_change"],
            stock = data["stock"],
            keepBuying = data["keepBuying"],
            last_change = data["last_change"],
            warehouse = data.get("warehouse")
        )

    def restore_all_variants(self, data):
        self.variants = data         

    def udpate():
        pass