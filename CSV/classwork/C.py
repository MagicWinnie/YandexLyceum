import csv
import sys

sys.stdin = open("messier.txt", "r")

arr = []
for line in sys.stdin:
    arr.append(line.strip().rstrip("\n").split("\t"))

with open("messier.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=";")
    for line in arr:
        spamwriter.writerow(line)
