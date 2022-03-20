import csv

d = {}
with open("in_file.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=";")
    for line in reader:
        if line[0] not in d:
            d[line[0]] = []
        d[line[0]].append(line[1])

start = ""
for key in d:
    if start != "":
        break
    for key_in in d:
        if key in d[key_in]:
            break
    else:
        start = key
        break

levels = {}


def dfs(v, level):
    if level not in levels:
        levels[level] = []
    levels[level].append(v)
    if v not in d:
        return
    for u in d[v]:
        dfs(u, level + 1)


dfs(start, 0)

with open("out_file.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter=";")
    for k in sorted(levels.keys()):
        writer.writerow(sorted(levels[k]))
