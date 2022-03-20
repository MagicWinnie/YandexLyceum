def cash_withdrawal(value):
    if value > 50_000:
        return "Exceeded the limit"
    sum_vals = sum(k * atm[k] for k in atm)
    if value > sum_vals:
        return "Insufficient funds"
    noms = sorted(list(atm.keys()), reverse=True)
    curr_sum = 0
    curr_nom = 0
    return_str = ""
    while curr_sum < value and curr_nom < len(noms):
        number_of = min((value - curr_sum) // noms[curr_nom], atm[noms[curr_nom]])
        if number_of != 0:
            curr_sum += noms[curr_nom] * number_of
            return_str += f"{number_of} bills of {noms[curr_nom]} rubles each\n"
        curr_nom += 1

    if curr_sum != value:
        return "Insufficient funds"

    return return_str


atm = {5000: 13, 2000: 16, 1: 2}
print(cash_withdrawal(1698))
