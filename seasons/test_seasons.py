from seasons import date_format
import pytest

def test_correct_format():
  assert date_format("2025-08-24") == "Five hundred twenty-five thousand, six hundred minutes"
  assert date_format("2024-08-24") == "One million, fifty-one thousand, two hundred minutes"

def test_sysexit():
  with pytest.raises(SystemExit) as sample:
    date_format("2025/08/14")