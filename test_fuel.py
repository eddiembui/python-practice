import fuel
import pytest

def test_convert():
    assert fuel.convert("3/4") == 75

def test_valuerror():
    with pytest.raises(ValueError):
        fuel.convert("s/r")

def test_negative_numbers():
    with pytest.raises(ValueError):
        fuel.convert("-3/-2")

def test_zero_ony():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")

def test_empty():
    assert fuel.gauge(1) == "E"

def test_full():
    assert fuel.gauge(99) == "F"

def test_any():
    assert fuel.gauge(45) == "45%"