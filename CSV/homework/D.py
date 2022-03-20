import csv
import sys

sys.stdin = open("in_file.txt", "r")


arr = []
header = ["id", "section", "h_dimension", "v_dimension", "price", "date"]
with open("posters.csv", "r", encoding="utf-8") as infile:
    reader = csv.reader(infile, delimiter=";")
    next(reader, None)
    for line in reader:
        arr.append(
            [int(line[0]), line[1], int(line[2]), int(line[3]), int(line[4]), line[5]]
        )

k = input()
arr.sort(key=lambda x: x[header.index(k)])

with open("sorted.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    for line in arr:
        writer.writerow(line)
