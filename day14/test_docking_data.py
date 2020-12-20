import pytest
from docking_data import encode, encode_address
from typing import List


@pytest.mark.parametrize(
    ["mask"],
    [pytest.param("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")]
)
@pytest.mark.parametrize(
    ["value", "expected_value"],
    [
        pytest.param(
            11,
            73,
            id="mask applied",
        ),
        pytest.param(
            101,
            101,
            id="no effect",
        ),
        pytest.param(
            0,
            64,
            id="mask applied again",
        ),
    ]
)
def test_encode(mask : str, value : int, expected_value : int) -> None:
    assert expected_value == encode(mask, value)


@pytest.mark.parametrize(
    ["mask", "value", "expected_value"],
    [
        pytest.param(
            "000000000000000000000000000000X1001X",
            42,
            [26, 27, 58, 59],
            id="example 1",
        ),
        pytest.param(
            "00000000000000000000000000000000X0XX",
            26,
            [16, 17, 18, 19, 24, 25, 26, 27],
            id="example 2",
        ),
    ]
)
def test_encode_address(mask : str, value : int, expected_value : List[int]) -> None:
    assert sorted(expected_value) == sorted(encode_address(mask, value))
