class Sandpile:
    def __init__(self, values=None):
        if values:
            self.table = [[values[x][y] for y in range(3)] for x in range(3)]
            self.check_over_flow()
        else:
            self.table = [[0 for _ in range(3)] for _ in range(3)]

    def __getitem__(self, x):
        return self.table[x]

    def __iter__(self):
        return self.table.__iter__()

    def __eq__(self, other):
        for x in range(3):
            for y in range(3):
                if self[x][y] != other[x][y]:
                    return False
        return True

    def __repr__(self):
        return '\n'.join([' '.join([str(col) for col in row]) for row in self.table])

    def __add__(self, other):
        s = Sandpile()
        for x in range(3):
            for y in range(3):
                s[x][y] = self[x][y] + other[x][y]
        s.check_over_flow()
        return s

    def check_over_flow(self):
        for i, row in enumerate(self.table):
            for j, col in enumerate(row):
                if col > 3:
                    self.over_flow(i, j)

    def over_flow(self, i, j):
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            try:
                self[i][j]-=1
                if x >= 0 and y >= 0:
                    self[x][y]+=1
            except IndexError:
                pass
        self.check_over_flow()

class MaxSandpile(Sandpile):
    def __init__(self):
        super().__init__([[3 for _ in range(3)] for _ in range(3)])

class SZeroSandpile(Sandpile):
    def __init__(self):
        super().__init__([[2,1,2],[1,0,1],[2,1,2]])

def is_set_s(pile):
    return pile + SZeroSandpile() == pile
