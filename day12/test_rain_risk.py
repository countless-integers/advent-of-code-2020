import pytest
from rain_risk import calculate_distance, move
from typing import List


@pytest.mark.parametrize(
    "instructions,expected_distance",
    [
        pytest.param(
            [
                "F10",
                "N3",
                "F7",
                "R90",
                "F11",
            ],
            25,
            id="example 1",
        ),
    ]
)
def test_calculate_distance(instructions : List[str], expected_distance : int) -> None:
    assert expected_distance == calculate_distance(instructions)
