import sys

k = int(input())

for line in sys.stdin:
    line = line.strip('\n')
    newline = ""
    for i in range(len(line)):
        newline += line[((k % len(line)) + i) % len(line)]
    print(newline)
