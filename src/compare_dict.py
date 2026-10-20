from deepdiff import DeepDiff


old_data = {
    "name": "Rodrigo",
    "age": 18,
    "address": {
        "name": "Rua imirim"
    },
    "father_name": "Luiz",
    "aunt":"Tia"
}

new_data = {
    "name": "Rodrigo",
    "age": 26,
    "address":{
        "name": "Rua Voluntarios",
        "number": 2831
    },
    "mother_name": "Eliza"
}


def compare_data(old, new):

    data_changed = DeepDiff(old, new)

    return data_changed


data = compare_data(old=old_data, new=new_data)

deleted_fields = list(data.get("dictionary_item_removed"))

for delete in deleted_fields:
    print(delete.split("'")[1])


# print(data.get("values_changed"))
print()
# print(data.get("dictionary_item_added"))
print()
# print(data.get("dictionary_item_removed"))
print()


{
    
    'dictionary_item_added': ["root['mother_name']", "root['address']['number']"],
      'values_changed': {"root['age']": {'new_value': 26, 'old_value': 18},
                          "root['address']['name']": {'new_value': 'Rua Voluntarios', 'old_value': 'Rua imirim'
                                                      }}}