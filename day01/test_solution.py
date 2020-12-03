import pytest
from solution import solve_first, solve_second

@pytest.mark.parametrize(
    "data,target_value,expected_product",
    [
        pytest.param([1, 2, 3, 4, 5], 8, 15, id="sorted list"),
        pytest.param([3, 5, 2, 4, 1], 8, 15, id="shuffled list"),
    ]
)
def test_solve_first(data, target_value, expected_product):
    assert expected_product == solve_first(data, target_value)


@pytest.mark.parametrize(
    "data,target_value,expected_product",
    [
        pytest.param([1, 2, 3, 4, 5], 8, 10, id="sorted list"),
        pytest.param([3, 5, 2, 4, 1], 8, 10, id="shuffled list"),
    ]
)
def test_solve_second(data, target_value, expected_product):
    assert expected_product == solve_second(data, target_value)