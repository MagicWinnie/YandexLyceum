import csv

thresh = int(input())

with open("vps.csv", newline="") as csvfile:
    csv_r = csv.reader(csvfile, delimiter=";")
    next(csv_r, None)
    for line in csv_r:
        if int(line[4]) >= thresh:
            print(line[0])
