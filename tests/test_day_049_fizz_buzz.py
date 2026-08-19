from solutions.day_049_fizz_buzz import fizz_buzz

def test_fizz_buzz_basic():
    result = fizz_buzz(3)
    assert result == ["1", "2", "Fizz"]

def test_fizz_buzz_five():
    result = fizz_buzz(5)
    assert result[4] == "Buzz"

def test_fizz_buzz_fifteen():
    result = fizz_buzz(15)
    assert result[14] == "FizzBuzz"

def test_fizz_buzz_single():
    assert fizz_buzz(1) == ["1"]