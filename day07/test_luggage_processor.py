import pytest
from luggage_processor import find_bags_containing, parse_row, count_bags_in_bags


@pytest.mark.parametrize(
    "bags,expected_count",
    [
        pytest.param(
            {
                "light red": {"bright white": 1, "muted yellow": 2},
                "dark orange": {"bright white": 3, "muted yellow": 4},
                "bright white": {"shiny gold": 1},
                "muted yellow": {"shiny gold": 2, "faded blue": 9},
                "shiny gold": {"dark olive": 1, "vibrant plum": 2},
                "dark olive": {"faded blue": 3, "dotted black": 4},
                "vibrant plum": {"faded blue": 5, "dotted black": 6},
                "faded blue": {},
                "dotted black": {},
            },
            4,
            id="example 1",
        ),
    ]
)
def test_find_bags_containing(bags : dict, expected_count : int) -> None:
    assert expected_count == len(find_bags_containing("shiny gold", bags))


@pytest.mark.parametrize(
    "row,expected_result",
    [
        pytest.param(
            "dotted black bags contain no other bags.",
            {"dotted black": {}}
        ),
        pytest.param(
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            {"vibrant plum": {
                "faded blue": 5,
                "dotted black": 6,
            }}
        )

    ]
)
def test_parse_row(row : str, expected_result : dict) -> None:
    assert expected_result == parse_row(row)


@pytest.mark.parametrize(
    "bags,expected_count",
    [
        pytest.param(
            {
                "light red": {"bright white": 1, "muted yellow": 2},
                "dark orange": {"bright white": 3, "muted yellow": 4},
                "bright white": {"shiny gold": 1},
                "muted yellow": {"shiny gold": 2, "faded blue": 9},
                "shiny gold": {"dark olive": 1, "vibrant plum": 2},
                "dark olive": {"faded blue": 3, "dotted black": 4},
                "vibrant plum": {"faded blue": 5, "dotted black": 6},
                "faded blue": {},
                "dotted black": {},
            },
            32,
            id="example 1"
        )
    ]
)
def test_count_bags_in_bags(bags : dict, expected_count : int) -> None:
    assert expected_count == count_bags_in_bags('shiny gold', bags)