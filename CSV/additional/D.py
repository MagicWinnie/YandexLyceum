from re import S
import sys
import csv

d = {}

for line in sys.stdin:
    dish_name, product_name, quantity = line.split("\t")
    quantity = int(quantity)
    if dish_name not in d:
        d[dish_name] = {}
    if product_name not in d[dish_name]:
        d[dish_name][product_name] = 0
    d[dish_name][product_name] += quantity

products = set()
for d_n in d:
    for p_n in d[d_n]:
        products.add(p_n)
products = sorted(list(products))

with open("recipes.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile, delimiter=";")
    writer.writerow(["recipe"] + products)
    for d_n in sorted(d.keys()):
        curr_line = [d_n]
        for p in products:
            curr_line.append(d[d_n].get(p, 0))
        writer.writerow(curr_line)
