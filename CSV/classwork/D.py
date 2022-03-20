import csv

state = input()
start, end = input().split()

arr = [["Субъект", start, end]]
with open("salary.csv", newline="", encoding="utf-8") as csvfile:
    csv_r = csv.DictReader(csvfile, delimiter=";")
    for line in csv_r:
        if line["Федеральный округ"] != state:
            continue
        if (int(line[end]) * 100 / int(line[start]) - 100) < 4:
            arr.append([line["Субъект"], line[start], line[end]])

with open("out_file.csv", mode="w", newline="", encoding="utf-8") as outfile:
    csv_w = csv.writer(outfile, delimiter=";")
    if len(arr) > 1:
        csv_w.writerows(arr)
