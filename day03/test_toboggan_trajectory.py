import pytest
from toboggan_trajectory import count_trees


@pytest.mark.parametrize(
    "slope,expected_count",
    [
        pytest.param((3, 1), 7, id="slope 3-1"),
        pytest.param((1, 1), 2, id="slope 1-1"),
        pytest.param((5, 1), 3, id="slope 5-1"),
        pytest.param((7, 1), 4, id="slope 7-1"),
        pytest.param((1, 2), 2, id="slope 1-2"),
    ]
)
def test_slope_run(slope : tuple, expected_count : int) -> None:
    landmap = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    assert expected_count == count_trees(landmap, slope)
