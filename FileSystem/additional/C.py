import sys

sys.stdin = open("pipes.txt", "r")
sys.stdout = open("time.txt", "w")

flag = True
by_themselves = []
used = []
for line in sys.stdin:
    line = line.strip().rstrip("\n")
    if line == "":
        flag = False
    if flag:
        by_themselves.append(float(line))
    else:
        used = list(map(int, line.split()))

s = 0
for i in used:
    s += 1 / by_themselves[i - 1]

print(1 / s * 60)
