import sys
import json

arr = []

for line in sys.stdin:
    arr.append(line)

d = json.load(open(arr[0].rstrip("\n")))

arr = arr[1:]

for i in range(len(arr)):
    arr[i] = list(map(int, arr[i].split("-")))

out = {}

for i in range(len(arr)):
    v = d[str(len(arr[i]))]
    k = str(i + 1)
    if v == "n":
        out[k] = sorted(list(filter(lambda x: (x <= 1000 and x % 10 == 1), arr[i])))
    elif v == "m":
        out[k] = sorted(list(filter(lambda x: (x % 3 == 0 or x % 7 == 0), arr[i])))
    else:
        out[k] = sorted(arr[i])

with open("misery.json", "w") as f:
    json.dump(out, f, indent=4)
