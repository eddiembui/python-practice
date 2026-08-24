from plates import is_valid

def test_two_letters():
    assert is_valid("CS") == True

def test_one_character():
    assert is_valid("C") == False

def test_six_characters():
    assert is_valid("AAA222") == True

def test_seven_characters():
    assert is_valid("AAAA222") == False

def test_middle_number():
    assert is_valid("AAA22A") == False

def test_punctuations():
    assert is_valid("AA{22") == False

def test_start_zero():
    assert is_valid("CS05") == False

def test_two_numbers():
    assert is_valid("50") == False