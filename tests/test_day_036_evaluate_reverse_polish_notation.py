from solutions.day_036_evaluate_reverse_polish_notation import eval_rpn

def test_eval_basic():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9

def test_eval_division():
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6

def test_eval_subtraction():
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22