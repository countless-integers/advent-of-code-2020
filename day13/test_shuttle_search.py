import pytest
from shuttle_search import find_connection, find_special_promotion
from typing import List


@pytest.mark.parametrize(
    ["timestamp", "bus_ids", "expected_connection"],
    [
        pytest.param(
            939,
            [7,13,"x","x",59,"x",31,19],
            {
                "id": 59,
                "wait": 5
            },
            id="example 1",
        ),
    ]
)
def test_find_connection(timestamp : int, bus_ids : List[int], expected_connection : dict) -> None:
    assert expected_connection == find_connection(timestamp, bus_ids)


@pytest.mark.parametrize(
    ["bus_ids", "expected_timestamp"],
    [
        pytest.param(
            [3, 7, 11, 5],
            867,
            id="example 1"
        ),
        pytest.param(
            [17,"x",13,19],
            3417,
            id="example 2"
        ),
        pytest.param(
            [7,13,"x","x",59,"x",31,19],
            1068781,
            id="example 3",
        ),
        pytest.param(
            [67,7,59,61],
            754018,
            id="example 4",
        ),
        pytest.param(
            [67,"x",7,59,61],
            779210,
            id="example 5",
        ),
        pytest.param(
            [67,7,"x",59,61],
            1261476,
            id="example 6",
        ),
        pytest.param(
            [1789,37,47,1889],
            1202161486,
            id="example 7",
        ),
    ]
)
def test_find_special_promotion(bus_ids : List[int], expected_timestamp : int) -> None:
    assert expected_timestamp == find_special_promotion(bus_ids)
