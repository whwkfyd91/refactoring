from example1.exam import hello

def func(x):
    return x + 1

def test_hello():
    hello()
    assert func(4) == 5
