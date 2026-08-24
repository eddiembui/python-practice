from twttr import shorten

def test_general_removal():
  assert shorten("mike") == "mk"

def test_duplicate_vowels():
  assert shorten("eddie") == "dd"

def test_capitalized():
  assert shorten("Empire") == "mpr"

def test_moit_numbers():
  assert shorten("mine23") == "mn23"

def test_omit_punctuation():
  assert shorten("eddie.") == "dd."

