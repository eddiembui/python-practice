from bank import value

def test_hello():
    assert value("Hello, sir") == 0

def test_h():
    assert value("Hey") == 20
def test_with_no_h():
    assert value("What's up!") == 100
def test_with_int():
    assert value("1") == 100
