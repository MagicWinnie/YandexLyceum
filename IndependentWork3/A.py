import sys

inp = input()
out = input()

sys.stdin = open(inp, 'r')
sys.stdout = open(out, 'w')

d = {}

for line in sys.stdin:
    tmp = line.split(':')
    d[tmp[0]] = int(tmp[1])

for k, v in sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True):
    print(k)
