import sys

sys.stdin = open("data.txt", "r")

n = int(input())
dels = list(map(int, input().split()))
dels.sort()

s = 0
for i in range(1, n):
    for d in dels:
        if i % d == 0:
            s += i
            break

print(s)
