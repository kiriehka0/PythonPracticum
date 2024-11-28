import json

json_name = input()
json_update = input()

with open(json_name) as file:
    source = json.load(file)
with open(json_update) as file:
    updates = json.load(file)

name_key = 'name'
new_dict = {}

for update in updates:
    for data in source:
        if update[name_key] == data[name_key]:
            for key in update.keys():
                if update[key] > data.get(key, ''):
                    data[key] = update[key]

for data in source:
    name = data.pop(name_key)
    new_dict[name] = data

with open(json_name, 'w') as file:
    json.dump(new_dict, file, sort_keys=False, indent=4, ensure_ascii=False)
