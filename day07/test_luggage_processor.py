import pytest
from luggage_processor import find_bags_containing, parse_row


@pytest.mark.parametrize(
    "bags,expected_count",
    [
        pytest.param(
            {
                "light red": ["bright white", "muted yellow"],
                "dark orange": ["bright white", "muted yellow"],
                "bright white": ["shiny gold"],
                "muted yellow": ["shiny gold", "faded blue"],
                "shiny gold": ["dark olive", "vibrant plum"],
                "dark olive": ["faded blue", "dotted black"],
                "vibrant plum": ["faded blue", "dotted black"],
                "faded blue": [],
                "dotted black": [],
            },
            4,
            id="example 1",
        ),
    ]
)
def test_find_bags_containing(bags : dict, expected_count : int) -> None:
    assert expected_count == len(find_bags_containing("shiny gold", bags))