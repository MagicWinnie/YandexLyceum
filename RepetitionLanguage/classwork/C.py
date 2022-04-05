a = int(input())
b = int(input())

count = 0
while True:
    if a == 0 or b == 0:
        break
    print(min(a, b), end=" ")
    if a > b:
        a -= b
    else:
        b -= a
    count += 1
print()
print(count)
