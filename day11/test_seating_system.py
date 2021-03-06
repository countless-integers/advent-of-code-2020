import pytest
from seating_system import run, run_again, count_occupied
from typing import List


@pytest.mark.parametrize(
    "initial_state,expected_steady_state",
    [
        pytest.param(
            [
                "L.LL.LL.LL",
                "LLLLLLL.LL",
                "L.L.L..L..",
                "LLLL.LL.LL",
                "L.LL.LL.LL",
                "L.LLLLL.LL",
                "..L.L.....",
                "LLLLLLLLLL",
                "L.LLLLLL.L",
                "L.LLLLL.LL",
            ],
            [
                "#.#L.L#.##",
                "#LLL#LL.L#",
                "L.#.L..#..",
                "#L##.##.L#",
                "#.#L.LL.LL",
                "#.#L#L#.##",
                "..L.L.....",
                "#L#L##L#L#",
                "#.LLLLLL.L",
                "#.#L#L#.##",
            ],
            id="example 1",
        ),
    ]
)
def test_get_differences(initial_state : List[str], expected_steady_state : List[str]) -> None:
    assert expected_steady_state == run(initial_state)


@pytest.mark.parametrize(
    "state,expected_count",
    [
        pytest.param(
            [
                "#.#L.L#.##",
                "#LLL#LL.L#",
                "L.#.L..#..",
                "#L##.##.L#",
                "#.#L.LL.LL",
                "#.#L#L#.##",
                "..L.L.....",
                "#L#L##L#L#",
                "#.LLLLLL.L",
                "#.#L#L#.##",
            ],
            37,
            id="example 1",
        ),
    ]
)
def test_run(state : List[str], expected_count : List[str]) -> None:
    assert expected_count == count_occupied(state)


@pytest.mark.parametrize(
    "initial_state,expected_steady_state",
    [
        pytest.param(
            [
                "L.LL.LL.LL",
                "LLLLLLL.LL",
                "L.L.L..L..",
                "LLLL.LL.LL",
                "L.LL.LL.LL",
                "L.LLLLL.LL",
                "..L.L.....",
                "LLLLLLLLLL",
                "L.LLLLLL.L",
                "L.LLLLL.LL",
            ],
            [
                "#.L#.L#.L#",
                "#LLLLLL.LL",
                "L.L.L..#..",
                "##L#.#L.L#",
                "L.L#.LL.L#",
                "#.LLLL#.LL",
                "..#.L.....",
                "LLL###LLL#",
                "#.LLLLL#.L",
                "#.L#LL#.L#",
            ],
            id="example 1",
        ),
    ]
)
def test_run_again(initial_state : List[str], expected_steady_state : List[str]) -> None:
    assert expected_steady_state == run_again(initial_state)
