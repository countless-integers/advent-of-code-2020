import pytest
from adapter_array import get_differences, count_arrangements


@pytest.mark.parametrize(
    "adapters,expected_differences",
    [
        pytest.param(
            [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4],
            {
                1: 7,
                2: 0,
                3: 5,
            },
            id="example 1",
        ),
        pytest.param(
            [
                28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 
                38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3,
            ],
            {
                1: 22,
                2: 0,
                3: 10,
            },
            id="example 2",
        ),
    ]
)
def test_get_differences(adapters : list, expected_differences : dict) -> None:
    assert expected_differences == get_differences(adapters)


@pytest.mark.parametrize(
    "adapters,expected_count",
    [
        pytest.param(
            [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4],
            8,
            id="example 1",
        ),
        pytest.param(
            [
                28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 
                38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3,
            ],
            19208,
            id="example 2",
        ),
    ]
)
def test_count_arrangements(adapters : list, expected_count : int) -> None:
    assert expected_count == count_arrangements(adapters)
