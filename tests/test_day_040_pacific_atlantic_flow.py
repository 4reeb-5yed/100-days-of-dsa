from solutions.day_040_pacific_atlantic_flow import pacific_atlantic

def test_pacific_atlantic_basic():
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    result = pacific_atlantic(heights)
    assert len(result) > 0
    assert [0,4] in result

def test_pacific_atlantic_small():
    heights = [[1,2],[3,4]]
    result = pacific_atlantic(heights)
    assert [1,1] in result