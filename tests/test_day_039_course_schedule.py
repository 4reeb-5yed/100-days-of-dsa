from solutions.day_039_course_schedule import can_finish

def test_can_finish():
    assert can_finish(2, [[1,0]]) == True

def test_cannot_finish():
    assert can_finish(2, [[1,0],[0,1]]) == False

def test_no_prerequisites():
    assert can_finish(3, []) == True