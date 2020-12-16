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
def test_find_connection(timestamp : int, bus_ids : list, expected_connection : dict) -> None:
    assert expected_connection == find_connection(timestamp, bus_ids)


@pytest.mark.parametrize(
    ["bus_ids", "expected_timestamp"],
    [
        pytest.param(
            [17,"x",13,19],
            3417,
            id="example 1"
        ),
        # pytest.param(
        #     [7,13,"x","x",59,"x",31,19],
        #     1068788,
        #     id="example 2",
        # ),
    ]
)
def test_find_special_promotion(bus_ids : list, expected_timestamp : int) -> None:
    assert expected_timestamp == find_special_promotion(bus_ids)