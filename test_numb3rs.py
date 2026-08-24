from numb3rs import validate

def test_single_digits():
  assert validate("2.2.2.2") == True

def test_double_digits():
  assert validate("22.22.22.22") == True

def test_triple_digits():
  assert validate("222.222.222.222") == True

def test_maximum_digits():
  assert validate("255.255.255.255") == True

def test_upper_boundary():
  assert validate("278.278.278.278") == False
  assert validate("278.278.278.27") == False
  assert validate("278.278.27.278") == False
  assert validate("278.27.278.278") == False
  assert validate("27.278.278.278") == False
  assert validate("278.27.27.27") == False
  assert validate("27.278.27.27") == False
  assert validate("27.27.278.27") == False
  assert validate("27.27.27.278") == False

def test_lower_boundary():
  assert validate("-2.-2.-2.-2") == False
  assert validate("-2.0.0.1") == False
  assert validate("2.-2.0.1") == False
  assert validate("2.2.-3.1") == False
  assert validate("2.2.3.-1") == False

def test_three():
  assert validate("2.2.2") == False

def test_five():
  assert validate("2.2.2.2.2") == False

def test_leading_zeros():
  assert validate("2.02.2.2") == False

def test_only_zeros():
  assert validate("2.0.0.1") == True