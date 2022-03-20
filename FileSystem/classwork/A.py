with open("sequence.txt", "r") as e:
    t = e.read().rstrip().replace("DF", "D F").split()
    print(max(list(map(len, t))))
