from itertools import chain
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
        return list(chain.from_iterable(self.table)) == list(chain.from_iterable(other))

    def __str__(self):
        return '\n'.join([' '.join([str(col) for col in row]) for row in self.table])

    def __add__(self, other):
        return Sandpile([[self[x][y]+other[x][y] for y in range(3)] for x in range(3)])

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
    """A representation of the most sand that can be held in a pile, or:
        3 3 3
        3 3 3
        3 3 3
    """
    def __init__(self):
        super().__init__([[3 for _ in range(3)] for _ in range(3)])

class SZeroSandpile(Sandpile):
    """If a sandpile is part of Set S then addition to SZeroSandpile while result in the original pile."""
    def __init__(self):
        super().__init__([[2,1,2],[1,0,1],[2,1,2]])

    @classmethod
    def is_set_s(cls, pile):
        return pile + cls() == pile
