from solutions.day_060_time_based_kv import TimeMap

def test_time_map_basic():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"

def test_time_map_multiple():
    tm = TimeMap()
    tm.set("a", "val", 1)
    tm.set("a", "val2", 3)
    assert tm.get("a", 1) == "val"
    assert tm.get("a", 2) == "val"
    assert tm.get("a", 3) == "val2"

def test_time_map_missing():
    tm = TimeMap()
    assert tm.get("missing", 1) == ""
