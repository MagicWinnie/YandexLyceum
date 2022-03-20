import csv
import sys

arr = []
for line in sys.stdin:
    arr.append(line.strip().rstrip("\n").split("\t"))

with open("plantis.csv", "w", newline="") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=";")
    spamwriter.writerow(
        [
            "nomen",
            "definitio",
            "pluma",
            "Russian nomen",
            "familia",
            "Russian nomen familia",
        ]
    )
    for line in arr:
        spamwriter.writerow(line)
