from collections import Counter


def molecule_assembly(*args, overwrite=False):
    global dna_chain
    compl = {"G": "C", "C": "G", "A": "T", "T": "A"}
    if len(args) == 0:
        return list(map(lambda x: "".join(x), molecule_dna))
    if len(args) == 2:
        if overwrite:
            dna_chain = dna
        else:
            dna_chain += dna
    c = Counter(args[0])
    n = len(dna_chain)
    for i in range(n):
        if c[compl[dna_chain[0]]] > 0:
            molecule_dna.append((dna_chain[0], compl[dna_chain[0]]))
            c[compl[dna_chain[0]]] -= 1
            dna_chain = dna_chain[1:]
        else:
            break
    return list(map(lambda x: "".join(x), molecule_dna))


molecule_dna = [("G", "C"), ("A", "T"), ("C", "G")]
dna_chain = "TGACACGTTACGACGG"
data = ["C", "G", "T", "C", "G", "A", "C", "G", "A", "C"]
dna = "CCAGAGTTCTTACGTGACTCACC"
print(" ".join(molecule_assembly(data, dna, overwrite=True)))
print()
data = ["A", "T", "C", "C", "A"]
dna = "GGTCTTCCGTTGC"
print(" ".join(molecule_assembly(data, dna)))
