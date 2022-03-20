import sys

sys.stdin = open("in_file.txt", "r")
sys.stdout = open("out_file.txt", "w")

d = int(input())
lines = []
lens = []
for line in sys.stdin:
    lines.append(line.strip().rstrip("\n"))
    lens.append(len(lines[-1]))

av = sum(lens) // len(lens)

print(av)

for i in range(len(lines)):
    if abs(av - lens[i]) <= d:
        print(lines[i])
