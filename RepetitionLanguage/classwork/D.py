from itertools import product

lst = list(
    map(
        lambda x: ''.join(x), list(product(sorted("АЛГОРИТМ"), repeat=5))
    )
)

string = input()
print(lst.index(string) + 1)
