from um import count

def test_one_um():
  assert count("um") == 1

def test_two_um():
  assert count("hello, um, world, um") == 2

def test_um_substring():
  assert count("yummy") == 0

def test_word_beginning_um():
  assert count("umpire") == 0

def test_word_ending_um():
  assert count("abrum") == 0

def test_word_beginning_and_ending_with_um():
  assert count("umpum") == 0

def test_umum():
  assert count("umum") == 0

def test_case_insensitive():
  assert count("Um, hello") == 1