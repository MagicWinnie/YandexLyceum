def dict_flip(*args):
    args = list(args)
    args = list(map(lambda x: x.decode("utf-8"), args))
    d = {}
    for i in range(1, len(args), 2):
        d[args[i]] = args[i - 1]
    return d
