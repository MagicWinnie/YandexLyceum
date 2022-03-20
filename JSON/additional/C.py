import json
import csv


def check_security(name, place):
    d = json.load(open("taxpayer_in.json", "r", encoding="utf-8"))
    tin = ""
    for el in d:
        if (
            el["lastname"] == name[0]
            and el["firstname"] == name[1]
            and el["middlename"] == name[2]
        ):
            tin = el["tin"]
            break
    else:
        return (None, None)

    region = -1
    with open("regions.csv", "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile, delimiter=";")
        for line in reader:
            if line["region_name"] == place:
                if line["region_code"] == tin[:2]:
                    region = 0
                break

    first_control = 0
    for i, v in enumerate([7, 2, 4, 10, 3, 5, 9, 4, 6, 8]):
        first_control += int(tin[i]) * v

    first_control %= 11
    first_control %= 10

    second_control = 0
    for i, v in enumerate([3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]):
        second_control += int(tin[i]) * v

    second_control %= 11
    second_control %= 10

    inn = str(first_control) == tin[10] and str(second_control) == tin[11]

    return region, 0 if inn else -1
