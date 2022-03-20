def vaccine_filter(func):
    i = 0
    while i < len(immunoglobulins):
        if not func(immunoglobulins[i]):
            del immunoglobulins[i]
        else:
            i += 1

immunoglobulins = [('IgE', 2), ('IgA', 3),
                   ('IgG', 17), ('IgF', 4),
                   ('IgX', 21), ('IgZ', 5)]
vaccine_filter(lambda x: x[1] > 4)
print(*immunoglobulins, sep='\n')