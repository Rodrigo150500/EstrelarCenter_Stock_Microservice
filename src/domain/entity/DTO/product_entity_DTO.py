from typing import TypedDict, NotRequired


class ProductCreateDTO(TypedDict):

    code: str
    description: str
    brand: NotRequired["str"]
    reference: NotRequired["str"]
    location: NotRequired[list["str"]]
    image: str
    measure: str
    quantity_change: int
    stock: int
    keepBuying: bool
    warehouse: NotRequired[WarehouseDTO]


class WarehouseDTO(TypedDict):

    quantity_change: int
    stock: int
    measure: str
    last_change: str
    location: list["str"]


class ProductCreateDTOResponse(TypedDict):

    _id: str
    brand: str
    description: str
    image: str
    keepBuying: bool
    last_change: str
    location: list["str"]
    measure: str
    quantity_change: int
    reference: str
    stock: int
    warehouse: NotRequired[WarehouseDTO]


class ProductUpdateDTO(TypedDict):

    brand: NotRequired["str"]
    description: NotRequired["str"]
    image: NotRequired["str"]
    keepBuying: NotRequired["bool"]
    last_change: NotRequired["str"]
    location: NotRequired[list["str"]]
    measure: NotRequired["str"]
    quantity_change: NotRequired["int"]
    reference: NotRequired["str"]
    stock: NotRequired["int"]
    warehouse: NotRequired[WarehouseDTO]


class ProductUpdateDTOResponse(TypedDict):

    brand: NotRequired["str"]
    description: NotRequired["str"]
    image: NotRequired["str"]
    keepBuying: NotRequired["bool"]
    last_change: NotRequired["str"]
    location: NotRequired[list["str"]]
    measure: NotRequired["str"]
    quantity_change: NotRequired["int"]
    reference: NotRequired["str"]
    stock: NotRequired["int"]
    warehouse: NotRequired[WarehouseDTO]
    last_change: str