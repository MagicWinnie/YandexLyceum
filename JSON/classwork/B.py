import json
import sys


d = {"complex": []}


for line in sys.stdin:
    line = line.strip().rstrip("\n")
    line = line.replace("- ", "-")
    line = line.replace("+ ", "+")
    d["complex"].append(
        {
            "Re": float(line.split()[2].replace("+", "")),
            "Im": float(line.split()[3].replace("+", "")),
        }
    )

with open("output.json", "w") as fp:
    json.dump(d, fp, indent=4)
