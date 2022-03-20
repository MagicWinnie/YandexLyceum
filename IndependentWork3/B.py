import csv

max_dist = int(input())

out = []

with open('still.csv', newline='') as csvfile:
    csv_d = csv.reader(csvfile, delimiter=',')
    for spamreader in csv_d:
        if spamreader[0] == 'id':
            continue
        if int(spamreader[-1]) <= max_dist and spamreader[2] == 'hill': 
            out.append([spamreader[1], int(spamreader[4]), int(spamreader[3]), int(spamreader[-1])])

out.sort(key=lambda x: (-x[1], -x[2], x[0]))

with open('hills.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='_')
    spamwriter.writerow(['name', 'height', 'distance', 'access'])
    for line in out:
        spamwriter.writerow(line)
