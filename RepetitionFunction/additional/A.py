import sys


def diff(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))


words = []

for line in sys.stdin:
    words.append(line.rstrip("\n"))

n = len(words)
prev = words[0]
last = words[-1]
words = words[:-1]
for i in range(n):
    for j in range(len(words)):
        if diff(prev, words[j]) <= 1:
            print(words[j])
            prev = words[j]
            del words[j]
            break

print(last)
