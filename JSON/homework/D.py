import csv
import json

d = {"type": {}}

with open("catalog.csv", "r", newline="") as infile:
    reader = csv.DictReader(infile, delimiter=";")
    for line in reader:
        if line["type"] not in d["type"]:
            d["type"][line["type"]] = {"breed": {}}
        if line["breed"] not in d["type"][line["type"]]["breed"]:
            d["type"][line["type"]]["breed"][line["breed"]] = []
        d["type"][line["type"]]["breed"][line["breed"]].append(
            {
                "name": line["name"],
                "age": line["age"],
                "gender": line["gender"],
                "owner": line["owner"],
                "phone": line["phone"],
            }
        )

json.dump(d, open("pets.json", "w"), indent=4)
