def color_search(*args, filename="output.txt"):
    # process input file
    with open("flower_drum.txt", "r", encoding="utf-8") as fp:
        raw_data = fp.readlines()
        raw_data = list(
            map(
                lambda x: " ".join(x.strip().strip("\n").replace("\t", " ").split()),
                raw_data,
            )
        )
    data = []
    for line in raw_data:
        hash_ind = line.index("#")
        name = line[: hash_ind - 1]
        hex_c = line[hash_ind: line.index(" ", hash_ind)]
        rgb = tuple(map(int, line.split()[-3:]))
        data.append([name, hex_c, rgb])
    # get the type of args
    t = 0  # 0 -- name, 1 -- hex, 2 -- rgb
    if "#" in args[0]:
        t = 1
    elif type(args[0]) == tuple:
        t = 2
    # process
    with open(filename, "w", encoding="utf-8") as o:
        for arg in args:
            for line in data:
                if line[t] != arg:
                    continue
                if t == 0:
                    o.write(
                        f"{line[0]}\t{line[1]}\t{line[2][0]}\t{line[2][1]}\t{line[2][2]}\n"
                    )
                elif t == 1:
                    o.write(
                        f"{line[1]}\t{line[0]}\t{line[2][0]}\t{line[2][1]}\t{line[2][2]}\n"
                    )
                else:
                    o.write(
                        f"{line[2][0]}\t{line[2][1]}\t{line[2][2]}\t{line[0]}\t{line[1]}\n"
                    )
                break
