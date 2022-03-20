import sys
import json

sys.stdin = open("input.txt", "r")

d = {}

count = 0
for line in sys.stdin:
    if line[0] not in d:
        d[line[0]] = 0
    d[line[0]] += 1
    count += 1

for key in d:
    d[key] /= count
    d[key] = round(d[key], 2)

json.dump(d, open("output.json", "w"), indent=4)
