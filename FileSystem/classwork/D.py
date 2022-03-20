import sys

filename = input()

morse = {}
with open(filename, "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip().strip("\n"), lines))
    for line in lines:
        char, code = line.split()
        morse[code] = char

for line in sys.stdin:
    print("".join(list(map(lambda x: morse[x], line.split()))))
