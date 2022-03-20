def big_data(*args, key=lambda x: x[0]):
    args = list(args)

    for i in range(len(args)):
        login = args[i][2].split("@")[0]
        login = login[0].upper() + login[1:].lower()
        date = args[i][1].split("-")
        login += date[0][0] + date[1][-1] + date[2][-1]
        args[i] += (login,)

    return sorted(args, key=key)
