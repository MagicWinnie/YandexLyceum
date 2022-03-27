class Genie:
    def __init__(self, n: int):
        self.n = n

    def get_beard(self) -> int:
        return self.n

    def __call__(self, wish: str, data, sort_order=False, step=1):
        if self.n - len(data) * len(data[0]) < 0:
            return
        self.n -= len(data) * len(data[0])

        if wish == "sort_rows":
            for i in range(0, len(data), step):
                data[i] = sorted(data[i], reverse=sort_order)
        elif wish == "sort_cols":
            for j in range(0, len(data[0]), step):
                tmp = sorted(
                    [data[i][j] for i in range(len(data))],
                    reverse=sort_order
                )
                for i in range(len(data)):
                    data[i][j] = tmp[i]
        elif wish == "sort_all":
            s = len(data[0])
            flatted = [item for sublist in data for item in sublist]
            tmp = []
            for i in range(0, len(flatted), step):
                tmp.append(flatted[i])
            tmp.sort(reverse=sort_order)
            ind = 0
            for i in range(0, len(flatted), step):
                flatted[i] = tmp[ind]
                ind += 1
            tmp_mat = [
                flatted[i: i + s] for i in range(0, len(flatted), s)
            ]
            for i in range(len(data)):
                for j in range(len(data[0])):
                    data[i][j] = tmp_mat[i][j]
