import sys

size_name = ("B", "KB", "MB", "GB", "TB")

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

files = {}
for line in sys.stdin:
    line = line.strip().strip("\n")
    filename = line.split()[0]
    ext = filename.split(".")[-1]
    size = line.split()[1:]
    size[0] = int(size[0])
    size[1] = size_name.index(size[1])
    if ext not in files:
        files[ext] = {}
    if filename not in files[ext]:
        files[ext][filename] = []
    files[ext][filename].append(size)

for ext in sorted(files.keys()):
    size_bytes = 0
    max_size = max(
        files[ext][
            max(files[ext], key=lambda x: max(files[ext].get(x), key=lambda y: y[1])[1])
        ],
        key=lambda z: z[1],
    )[1]
    for filename in sorted(files[ext].keys()):
        for sizes in files[ext][filename]:
            print(filename)
            size_bytes += sizes[0] / (1024 ** (max_size - sizes[1]))
    print("----------")
    size_bytes = round(size_bytes)
    if size_bytes >= 1024:
        print(f"Summary: {round(size_bytes / 1024)} {size_name[max_size + 1]}")
    else:
        print(f"Summary: {size_bytes} {size_name[max_size]}")
    print()
