import csv


def messier_search(param):
    s = set()
    with open("messier.csv", "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for line in reader:
            if line[param]:
                s.add(line[param])
    return sorted(list(s))
