import sys

hits = []
i = 1
for line in sys.stdin:
    if int(line.rstrip("\n")) == i:
        hits.append(i)
    i += 1

with open("output.txt", "w") as f:
    if len(hits) == 0:
        f.write("0")
    else:
        f.write(" ".join(list(map(str, hits))))
