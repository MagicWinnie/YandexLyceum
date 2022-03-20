def vaccine_effect(value):
    i = 0
    while i < len(immunoglobulins):
        if immunoglobulins[i][1] < value:
            del immunoglobulins[i]
        else:
            i += 1

immunoglobulins = [('IgE', 2), ('IgA', 3),
                   ('IgG', 17), ('IgF', 4),
                   ('IgX', 21), ('IgZ', 5)]
vaccine_effect(5)
print(*immunoglobulins, sep='\n')
