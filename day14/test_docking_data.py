import pytest
from docking_data import encode


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
def test_calculate_distance(mask : str, value : int, expected_value : int) -> None:
    assert expected_value == encode(mask, value)