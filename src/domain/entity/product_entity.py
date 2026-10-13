from datetime import datetime

from bson.objectid import ObjectId

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

class ProductEntity:

    @staticmethod
    def create(data):

        product_required_fields = ["code", "description", "image", "measure", "quantity_change", "stock", "keepBuying"]
        warehouse_required_fields = ["quantity_change", "stock", "measure"]

        measure_allowed = ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"]

        #Produto validação
        #Verificação de campos obrigatórios
        for field in product_required_fields:
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
                raise HttpUnprocessableEntity(message=f"O campo Estoque do Galpão não pode ser negativo")

            if data["warehouse"]["measure"] not in measure_allowed:
                        raise HttpUnprocessableEntity(message=f"O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote")

        _id = ObjectId()
        last_change = datetime.now()

        return {
            "_id": _id,
            "code": data["code"],
            "brand": data.get("brand"),
            "description": data["description"],
            "image": data["image"],
            "keepBuying": data["keepBuying"],
            "last_change": last_change,
            "location": data.get("location"),
            "measure": data["measure"],
            "quantity_change": data["quantity_change"],
            "reference": data["reference"],
            "stock": data["stock"],
            "warehouse": data.get("warehouse")
        }

    @staticmethod
    def update(new_data: dict):

        product_required_fields = ["code", "description", "image", "measure", "quantity_change", "stock", "keepBuying"]
        warehouse_required_fields = ["quantity_change", "stock", "measure"]

        measure_allowed = ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"]

        #Produto validação
        #Verificação de campos obrigatórios
        for key, value in new_data.items():

            if key in product_required_fields and value == "":
                raise HttpUnprocessableEntity(message=f"O campo {key} não pode estar vazio")
        
        if "measure" in new_data and new_data["measure"] not in measure_allowed:
            raise HttpUnprocessableEntity(message=f"O campo Medida deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote")

        if "stock" in new_data and new_data["stock"] < 0:
            raise HttpUnprocessableEntity(message=f"O campo Estoque não pode ser negativo")


        #Warehouse validação
        #Verificação de campos obrigatórios em warehouse
        if "warehouse" in new_data:
            for key, value in new_data["warehouse"].items():

                if key in warehouse_required_fields and value == "":
                    raise HttpUnprocessableEntity(message=f"O campo {key} não pode estar vazio")

            if "stock" in new_data["warehouse"] and new_data["stock"] < 0:
                raise HttpUnprocessableEntity(message=f"O campo Estoque não pode ser negativo")

            if "measure" in new_data["warehouse"] and new_data["measure"] not in measure_allowed:
                raise HttpUnprocessableEntity(message=f"O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote")

        if "code" in new_data:
            raise HttpUnprocessableEntity(message=f"O campo Code não pode ser atualizado")

        return {
            **new_data,
            "last_change": datetime.now()
        }