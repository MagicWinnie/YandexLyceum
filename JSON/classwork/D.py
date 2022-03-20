import csv
import json

d = {"dragons": []}

with open("dragons.csv", "r", newline="") as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    for line in reader:
        d["dragons"].append({key: line[i] for (i, key) in enumerate(header)})

json.dump(d, open("dragons.json", "w"), indent=4)
