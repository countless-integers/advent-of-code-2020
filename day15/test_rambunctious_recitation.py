import pytest
from rambunctious_recitation import play


@pytest.mark.parametrize(
    ["game_input", "turns", "expected_value"],
    [
        pytest.param([0,3,6], 10, 0, id="example 1"),
        pytest.param([0,3,6], 2020, 436, id="example 2"),
        pytest.param([1,3,2], 2020, 1, id="example 3"),
        pytest.param([2,1,3], 2020, 10, id="example 4"),
        pytest.param([1,2,3], 2020, 27, id="example 5"),
        pytest.param([2,3,1], 2020, 78, id="example 6"),
        pytest.param([3,2,1], 2020, 438, id="example 7"),
        pytest.param([3,1,2], 2020, 1836, id="example 8"),
    ]
)
def test_method(game_input : int, turns : int, expected_value: int) -> None:
    for number in play(game_input, turn_limit=turns):
        pass

    assert expected_value == number
