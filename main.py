import json

path = 'data/terra/phoenix-1/projects.json'

projects = json.load(open(path))

contracts = []

for project in projects:
    for contract in project["contracts"]:
        contracts.append({"slug": project["slug"], "name": contract['name'], "address": contract['address'], "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eleifend."})

with open('data/terra/phoenix-1/contracts.json', 'w') as outfile:
    json.dump(contracts, outfile, indent=2)