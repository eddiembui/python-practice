from jar import Jar
import pytest

def test_init():
  jar = Jar()
  assert jar.capacity == 12

def test_str():
  jar = Jar()
  assert str(jar) == ""
  jar.deposit(1)
  assert str(jar) == "🍪"
  jar.deposit(2)
  assert str(jar) == "🍪🍪🍪"

def test_deposit():
  jar = Jar()
  jar.deposit(2)
  with pytest.raises(ValueError) as sample:
    jar.deposit(11)
  jar = Jar()
  jar.deposit(5)
  assert jar.size == 5

def test_withdraw():
  jar = Jar()

  jar.deposit(7)
  jar.withdraw(3)
  assert jar.size == 4
  with pytest.raises(ValueError) as sample:
    jar.withdraw(6)





