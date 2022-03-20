s = input()

with open(s, "rb") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.decode().rstrip("\n"), lines))

with open("output.dat", "wb") as o:
    for line in lines:
        o.write((line[::-1] + "\n").encode())
