from solutions.day_058_decode_ways import num_decodings

def test_decode_ways_basic():
    assert num_decodings("12") == 2

def test_decode_ways_zero():
    assert num_decodings("226") == 3

def test_decode_ways_invalid():
    assert num_decodings("06") == 0

def test_decode_ways_single():
    assert num_decodings("1") == 1