from dataclasses import dataclass

from bson.objectid import ObjectId

@dataclass
class InsertProductInterface:

    inserted_id: ObjectId
    acknowledged: bool