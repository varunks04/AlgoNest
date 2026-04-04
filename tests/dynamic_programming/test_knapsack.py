from algonest.dynamic_programming import knapsack_01, unbounded_knapsack


def test_knapsack() -> None:
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    assert knapsack_01(weights, values, 7) == 9
    assert unbounded_knapsack(weights, values, 7) == 9
