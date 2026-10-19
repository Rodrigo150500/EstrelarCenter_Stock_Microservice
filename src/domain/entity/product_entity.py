from datetime import datetime

from bson.objectid import ObjectId

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.domain.entity.interfaces.product_entity_interface import ProductEntityInterface
from src.domain.entity.DTO.product_entity_DTO import ProductCreateDTO, ProductCreateDTOResponse, ProductUpdateDTO, ProductUpdateDTOResponse

class ProductEntity(ProductEntityInterface):

    @staticmethod
    def create(data: ProductCreateDTO) -> ProductCreateDTOResponse:

        product_fields_allowed = ["code", "description", "brand", "reference", "location", "image", "measure", "quantity_change", "stock", "keepBuying", "warehouse"]
        warehouse_fields_allowed = ["quantity_change", "stock", "measure", "location"]

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

        for field, _ in data.items():
            if field not in product_fields_allowed:
                raise HttpUnprocessableEntity(message=f"O campo {field} não pode ser incluso")
            

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

            for field, _ in data["warehouse"].items():
                if field not in warehouse_fields_allowed:
                    raise HttpUnprocessableEntity(message=f"O campo {field} não pode ser incluso no Galpão")
            
            if data["warehouse"]["stock"] < 0:
                raise HttpUnprocessableEntity(message=f"O campo Estoque do Galpão não pode ser negativo")

            if data["warehouse"]["measure"] not in measure_allowed:
                raise HttpUnprocessableEntity(message=f"O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote")

            data_warehouse = {**data["warehouse"], "last_change": datetime.now()}

            return {
                "_id": ObjectId(),
                **data,
                "last_change": datetime.now(),
                "warehouse": data_warehouse
            } 


        return {
            "_id": ObjectId(),
            "brand": data.get("brand"),
            "description": data["description"],
            "image": data["image"],
            "keepBuying": data["keepBuying"],
            "last_change": datetime.now(),
            "location": data.get("location"),
            "measure": data["measure"],
            "quantity_change": data["quantity_change"],
            "reference": data["reference"],
            "stock": data["stock"]
        }

    @staticmethod
    def update(new_data: ProductUpdateDTO) -> ProductUpdateDTOResponse:

        product_fields_allowed = ["code", "description", "brand", "reference", "location", "image", "measure", "quantity_change", "stock", "keepBuying", "warehouse"]
        warehouse_fields_allowed = ["quantity_change", "stock", "measure", "location"]

        product_required_fields = ["code", "description", "image", "measure", "quantity_change", "stock", "keepBuying"]
        warehouse_required_fields = ["quantity_change", "stock", "measure"]

        measure_allowed = ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"]

        if "code" in new_data:
            raise HttpUnprocessableEntity(message=f"O campo Code não pode ser atualizado")

        #Produto validação
        #Verificação de campos obrigatórios
        for key, value in new_data.items():

            if key in product_required_fields and value == "":
                raise HttpUnprocessableEntity(message=f"O campo {key} não pode estar vazio")

            if key not in product_fields_allowed:
                raise HttpUnprocessableEntity(message=f"O campo {key} não pode ser incluso")

        
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

                if key not in warehouse_fields_allowed:
                    raise HttpUnprocessableEntity(message=f"O campo {key} não pode ser incluso")


            if "stock" in new_data["warehouse"] and new_data['warehouse']["stock"] < 0:
                raise HttpUnprocessableEntity(message=f"O campo Estoque não pode ser negativo")

            if "measure" in new_data["warehouse"] and new_data["measure"] not in measure_allowed:
                raise HttpUnprocessableEntity(message=f"O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote")


            data_warehouse = new_data["warehouse"]
            data_warehouse["last_change"] = datetime.now()

            return {
                **new_data,
                "warehouse": data_warehouse,
                "last_change": datetime.now()
            }
                   
        return {
            **new_data,
            "last_change": datetime.now()
        }

