import pytest
from boot_sequence import boot


@pytest.mark.parametrize(
    "instructions,expected_acc",
    [
        pytest.param(
            [
                ["nop", "+0"],
                ["acc", "+1"],
                ["jmp", "+4"],
                ["acc", "+3"],
                ["jmp", "-3"],
                ["acc", "-99"],
                ["acc", "+1"],
                ["jmp", "-4"],
                ["acc", "+6"],
            ],
            5,
            id="example 1",
        ),
    ]
)
def test_find_bags_containing(instructions : list, expected_acc : int) -> None:
    assert expected_acc == boot(instructions)