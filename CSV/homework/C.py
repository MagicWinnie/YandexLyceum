import csv
import sys

sys.stdout = open("predict.txt", "w")


arr = []
with open("yndx_share_price.csv", "r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile, delimiter=",")
    for line in reader:
        arr.append(line["price"])

for i in range(len(arr)):
    max_ind = i
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            max_ind = j
            break
    print(max_ind - i, end=" ")
