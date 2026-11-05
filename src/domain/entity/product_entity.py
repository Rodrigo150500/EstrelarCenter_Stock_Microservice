
from datetime import datetime
from copy import deepcopy

from bson.objectid import ObjectId

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.domain.entity.interfaces.product_entity_interface import ProductEntityInterface
from src.domain.entity.DTO.product_entity_DTO import (
    ProductCreateDTO,
    ProductCreateDTOResponse,
    ProductUpdateDTO,
    ProductUpdateDTOResponse
)


class ProductEntity(ProductEntityInterface):

    PRODUCT_FIELDS_ALLOWED = [
        "code", "description", "brand", "reference", "location",
        "image", "measure", "quantity_change", "stock",
        "keepBuying", "warehouse"
    ]

    WAREHOUSE_FIELDS_ALLOWED = [
        "quantity_change", "stock", "measure", "location"
    ]

    PRODUCT_REQUIRED_FIELDS = [
        "code", "description", "image", "measure",
        "quantity_change", "stock", "keepBuying"
    ]

    WAREHOUSE_REQUIRED_FIELDS = [
        "quantity_change", "stock", "measure"
    ]

    MEASURE_ALLOWED = [
        "Unidade", "Caixa", "Pacote", "Fardo", "Saco",
        "Rolo", "Cartela", "Bloco", "Pote"
    ]

    @staticmethod
    def _validate_product(data: dict, creating: bool = False):

        for field in data:

            if field not in ProductEntity.PRODUCT_FIELDS_ALLOWED:
                raise HttpUnprocessableEntity(
                    message=f"O campo {field} não pode ser incluso"
                )

            if field in ProductEntity.PRODUCT_REQUIRED_FIELDS and data[field] == "":
                raise HttpUnprocessableEntity(
                    message=f"O campo {field} não pode estar vazio"
                )

        if creating:
            for field in ProductEntity.PRODUCT_REQUIRED_FIELDS:
                if field not in data:
                    raise HttpUnprocessableEntity(
                        message=f"Campo obrigatório: [{field}] não encontrado"
                    )

        if "measure" in data and data["measure"] not in ProductEntity.MEASURE_ALLOWED:
            raise HttpUnprocessableEntity(
                message=f"O campo Medida deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote"
            )

        if "stock" in data and data["stock"] < 0:
            raise HttpUnprocessableEntity(
                message=f"O campo Estoque não pode ser negativo"
            )

    @staticmethod
    def _validate_warehouse(data: dict, creating: bool = False):

        for field, value in data.items():

            if field not in ProductEntity.WAREHOUSE_FIELDS_ALLOWED:
                raise HttpUnprocessableEntity(
                    message=f"O campo {field} não pode ser incluso no Galpão"
                )

            if field in ProductEntity.WAREHOUSE_REQUIRED_FIELDS and value == "":
                raise HttpUnprocessableEntity(
                    message=f"O campo {field} não pode estar vazio"
                )

        if creating:
            for field in ProductEntity.WAREHOUSE_REQUIRED_FIELDS:
                if field not in data:
                    raise HttpUnprocessableEntity(
                        message=f"Campo obrigatório: [{field}] não encontrado"
                    )

        if "stock" in data and data["stock"] < 0:
            raise HttpUnprocessableEntity(
                message=f"O campo Estoque do Galpão não pode ser negativo"
            )

        if "measure" in data and data["measure"] not in ProductEntity.MEASURE_ALLOWED:
            raise HttpUnprocessableEntity(
                message=f"O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote"
            )

    @staticmethod
    def _get_changed_fields(new_data: dict, old_data: dict) -> dict:

        data_to_save = {}

        for key, value in new_data.items():

            old_value = old_data.get(key)

            if isinstance(value, dict) and isinstance(old_value, dict):

                changed_fields = ProductEntity._get_changed_fields(
                    value,
                    old_value
                )

                if changed_fields:
                    data_to_save[key] = changed_fields

            elif key not in old_data or value != old_value:
                data_to_save[key] = value

        return data_to_save

    @staticmethod
    def create(data: ProductCreateDTO) -> ProductCreateDTOResponse:

        data = deepcopy(data)

        ProductEntity._validate_product(data, creating=True)

        if "warehouse" in data:
            ProductEntity._validate_warehouse(
                data["warehouse"],
                creating=True
            )

        now = datetime.now()

        response = {
            "_id": ObjectId(),
            **data,
            "last_change": now
        }

        if "warehouse" in data:
            response["warehouse"]["last_change"] = now

        return response

    @staticmethod
    def update(
        new_data: ProductUpdateDTO,
        old_data: dict
    ) -> ProductUpdateDTOResponse:

        new_data = deepcopy(new_data)

        if "code" in new_data:
            raise HttpUnprocessableEntity(
                message=f"O campo Code não pode ser atualizado"
            )

        # Produto validação
        ProductEntity._validate_product(new_data)

        # Warehouse validação
        if "warehouse" in new_data:
            ProductEntity._validate_warehouse(new_data["warehouse"])

        # Comparação dos dados
        data_to_save = ProductEntity._get_changed_fields(
            new_data,
            old_data
        )

        # Nenhuma alteração encontrada
        if not data_to_save:
            return {}

        now = datetime.now()

        data_to_save["last_change"] = now

        if "warehouse" in data_to_save:
            data_to_save["warehouse"]["last_change"] = now

        return data_to_save
