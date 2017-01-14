from sandpile import Sandpile, MaxSandpile

def test_init():
    s = Sandpile()
    for x in range(3):
        for y in range(3):
            assert s[x][y] == 0

def test_init_arg():
    arg = [[1, 2, 3], [3, 2, 1], [2, 2, 2]]
    s = Sandpile(arg)
    for x in range(3):
        for y in range(3):
            assert s[x][y] == arg[x][y]

def test_add():
    assert Sandpile([[1,1,1], [1,1,1],[1,1,1]]) + Sandpile([[1,1,1], [1,1,1],[1,1,1]]) == [[2,2,2],[2,2,2],[2,2,2]]

def test_over_flow():
    s = Sandpile([[3 for _ in range(3)] for _ in range(3)])
    p = Sandpile([[0,0,0],[0,1,0],[0,0,0]])
    assert (s + p).table == [
        [1,3,1],
        [3,0,3],
        [1,3,1]
    ]

def test_max_pile():
    assert MaxSandpile() == [[3,3,3],[3,3,3],[3,3,3]]

def test_max_over_flow():
    assert (MaxSandpile() + Sandpile([[1,3,1],[3,3,3],[1,3,1]])) == [[2,2,2],[2,2,2],[2,2,2]]

# def test_is_set_s():
#     assert SZeroSandpile.is_set_s(MaxSandpile())
