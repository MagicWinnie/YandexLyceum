import json

d = json.load(open("input.json", "r"))

d.sort(
    key=lambda x: (
        -len(x["colors"]),
        -x["radius"],
        -((x["x"] ** 2 + x["y"] ** 2) ** 0.5),
        -x["id"],
    )
)

for e in d:
    print(e["id"], end=" ")
