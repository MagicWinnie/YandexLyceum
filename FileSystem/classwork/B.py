with open("in_file.txt", "r") as e, open("out_file.txt", "w") as o:
    q = e.readlines()
    for i in q:
        o.write(i.strip() + str(" = ") + str(eval(i)) + "\n")
