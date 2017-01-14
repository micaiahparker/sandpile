from sandpile import Sandpile, MaxSandpile

def test_init():
    s = Sandpile()
    for x in range(3):
        for y in range(3):
            assert s[x][y] == 0

def test_init_arg():
    arg = [[1, 2, 3], [3, 2, 1], [2, 2, 2]]
    s = Sandpile.from_list(arg)
    for x in range(3):
        for y in range(3):
            assert s[x][y] == arg[x][y]

def test_add():
    assert Sandpile(fill=1) + Sandpile(fill=1) == [[2,2,2], [2,2,2], [2,2,2]]

def test_over_flow():
    s = Sandpile.from_list([[0,0,0],[0,1,0],[0,0,0]])
    m = MaxSandpile() # 3x3 fill=3
    assert (s + m) == [
        [1,3,1],
        [3,0,3],
        [1,3,1]
    ]

def test_max_pile():
    assert MaxSandpile() == [[3,3,3],[3,3,3],[3,3,3]]

def test_max_over_flow():
    assert (MaxSandpile() + Sandpile.from_list([[1,3,1],[3,3,3],[1,3,1]])) == [[2,2,2],[2,2,2],[2,2,2]]

def test_asymmetric_add():
    assert Sandpile(cols=4)+MaxSandpile(cols=4)

# def test_is_set_s():
#     assert SZeroSandpile.is_set_s(MaxSandpile())
