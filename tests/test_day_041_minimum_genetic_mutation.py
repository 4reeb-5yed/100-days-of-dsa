from solutions.day_041_minimum_genetic_mutation import min_mutation

def test_min_mutation_basic():
    assert min_mutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1

def test_min_mutation_multi():
    result = min_mutation("AACCGGTT", "AACCGCTT", ["AACCGGTT", "AACCGCTT"])
    assert result == 1  # direct from bank

def test_min_mutation_impossible():
    assert min_mutation("AAAAACCC", "CCCCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]) == -1