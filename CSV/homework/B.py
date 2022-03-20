import csv
import sys


n, m = map(int, input().split())

with open("exam.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(
        ["Фамилия", "имя", "результат 1", "результат 2", "результат 3", "сумма"]
    )
    for line in sys.stdin:
        line = line.split()
        if int(line[2]) >= m and int(line[3]) >= m and int(line[4]) >= m:
            s = int(line[2]) + int(line[3]) + int(line[4])
            if s >= n:
                writer.writerow(line + [s])
