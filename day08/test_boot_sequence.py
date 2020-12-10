import pytest
from boot_sequence import boot, uno_boot


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
def test_boot(instructions : list, expected_acc : int) -> None:
    assert expected_acc == boot(instructions)


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
            8,
            id="replace 8th jmp with nop",
        ),
    ]
)
def test_boot_uno(instructions : list, expected_acc : int) -> None:
    assert expected_acc == uno_boot(instructions)