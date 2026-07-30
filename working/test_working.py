from working import convert
import pytest 

def test_bothAM():
  assert convert("9:05 AM to 10:05 AM") == "09:05 to 10:05"

def test_bothPM():
  assert convert("1:25 PM to 5:25 PM") == "13:25 to 17:25"

def test_AM_to_PM():
  assert convert("9:25 AM to 4:34 PM") == "09:25 to 16:34"

def test_PM_to_AM():
  assert convert("9:25 PM to 4:34 AM") == "21:25 to 04:34"

def test_without_min():
  assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_left_without_min():
  assert convert("10 AM to 4:26 PM") == "10:00 to 16:26"

def test_right_without_min():
  assert convert("10:34 AM to 5 PM") == "10:34 to 17:00"

def test_boundary():
  with pytest.raises(ValueError):
    convert("10:67 AM to 5:34 PM")

def test_right_boundary():
  with pytest.raises(ValueError):
      convert("10:24 AM to 5:78 PM")

def test_wrong_format():
  with pytest.raises(ValueError):
      convert("10:37 AM - 5:34 PM")
  with pytest.raises(ValueError):
      convert("10?37 AM to 5?34 PM")