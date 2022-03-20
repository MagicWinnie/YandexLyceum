import csv
import sys

sys.stdout = open("result.txt", "w")

arr = []
header = ["date", "time", "luminosity", "color"]
with open("alpha_oriona.csv", "r", encoding="utf-8") as infile:
    reader = csv.reader(infile, delimiter=";")
    next(reader, None)
    for line in reader:
        arr.append(line[:-2] + [int(line[-2])])

arr = arr + [["", "", 111111111111]]
max_len = -float("inf")
max_len_date = ["", ""]
curr_len = 0
curr_date = arr[0][:2]
for i in range(len(arr) - 1):
    if arr[i][2] >= arr[i + 1][2]:
        curr_len += 1
    else:
        if curr_len + 1 > max_len:
            max_len = curr_len + 1
            max_len_date = curr_date.copy()
        curr_len = 0
        curr_date = arr[i + 1][:2]
print(max_len)
print(*max_len_date)
