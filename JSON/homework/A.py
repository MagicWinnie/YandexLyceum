import sys
import json

d = {}

for line in sys.stdin:
    line = line.rstrip("\n")
    curr_num = int(line)
    age = 0
    while curr_num >= 10:
        tmp_num = 1
        for i in str(curr_num):
            tmp_num *= int(i)
        curr_num = tmp_num
        age += 1
    if int(line) < 10:
        age = 1
    if age not in d:
        d[age] = []
    d[age].append(line)

json.dump(d, open("numbers_age.json", "w"), indent=4)
