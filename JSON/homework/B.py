import sys
import json

sys.stdin = open("russian_words.txt", "r")

d = {}

for line in sys.stdin:
    line = line.strip("\n")
    if line[0] not in d:
        d[line[0]] = []
    d[line[0]].append(line)

json.dump(d, open("russian_words.json", "w"), indent=4)
