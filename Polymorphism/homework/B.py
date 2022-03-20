from copy import copy


class RightMirror:
    def __init__(self, matrix):
        self.matrix = copy(matrix)

    def reflect(self):
        for i in range(len(self.matrix)):
            self.matrix[i] = list(reversed(self.matrix[i]))


class BottomMirror:
    def __init__(self, matrix):
        self.matrix = copy(matrix)

    def reflect(self):
        new_mat = []
        for i in range(len(self.matrix) - 1, -1, -1):
            new_mat.append(self.matrix[i])
        self.matrix = new_mat
