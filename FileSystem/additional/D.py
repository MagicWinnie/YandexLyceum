import sys


def make_gradient(corner):
    sys.stdin = open("in.txt", "r")
    sys.stdout = open("gradient.txt", "w")
    mat = []
    for line in sys.stdin:
        mat.append(list(map(int, line.strip().rstrip("\n").split())))
    out = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    if corner == 0:
        out[0][0] = mat[0][0]
        for i in range(1, len(mat)):
            out[i][0] = mat[i][0] - mat[i - 1][0]
        for j in range(1, len(mat[0])):
            out[0][j] = mat[0][j] - mat[0][j - 1]
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                out[i][j] = mat[i][j] - mat[i - 1][j - 1]
    elif corner == 2:
        out[len(mat) - 1][len(mat[0]) - 1] = mat[len(mat) - 1][len(mat[0]) - 1]
        for i in range(len(mat) - 2, -1, -1):
            out[i][len(mat[0]) - 1] = (
                mat[i][len(mat[0]) - 1] - mat[i + 1][len(mat[0]) - 1]
            )
        for j in range(len(mat[0]) - 2, -1, -1):
            out[len(mat) - 1][j] = mat[len(mat) - 1][j] - mat[len(mat) - 1][j + 1]
        for i in range(len(mat) - 2, -1, -1):
            for j in range(len(mat[0]) - 2, -1, -1):
                out[i][j] = mat[i][j] - mat[i + 1][j + 1]
    elif corner == 1:
        out[0][len(mat[0]) - 1] = mat[0][len(mat[0]) - 1]
        for i in range(1, len(mat)):
            out[i][len(mat[0]) - 1] = (
                mat[i][len(mat[0]) - 1] - mat[i - 1][len(mat[0]) - 1]
            )
        for j in range(len(mat[0]) - 2, -1, -1):
            out[0][j] = mat[0][j] - mat[0][j + 1]
        for i in range(1, len(mat)):
            for j in range(len(mat[0]) - 2, -1, -1):
                out[i][j] = mat[i][j] - mat[i - 1][j + 1]
    else:
        out[len(mat) - 1][0] = mat[len(mat) - 1][0]
        for i in range(len(mat) - 2, -1, -1):
            out[i][0] = mat[i][0] - mat[i + 1][0]
        for j in range(1, len(mat[0])):
            out[len(mat) - 1][j] = mat[len(mat) - 1][j] - mat[len(mat) - 1][j - 1]
        for i in range(len(mat) - 2, -1, -1):
            for j in range(1, len(mat[0])):
                out[i][j] = mat[i][j] - mat[i + 1][j - 1]
    for l in out:
        print(*l, sep="\t")
