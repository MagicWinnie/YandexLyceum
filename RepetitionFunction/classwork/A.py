def genome(s1: str, s2: str):
    count = 0
    gen = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    for i in range(len(s1)):
        if gen[s1[i]] == s2[i]:
            count += 1
    return (count, True if count / len(s1) >= 0.7 else False)
