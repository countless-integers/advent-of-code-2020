import pytest
from xmas_encoder import find_error, find_elements, find_error_elements


@pytest.mark.parametrize(
    "numbers,target_sum,expected_elements",
    [
        pytest.param(
            [35, 20, 15, 25, 47],
            40,
            (15, 25),
            id="example 1",
        ),
        pytest.param(
            [95, 102, 117, 150, 182],
            127,
            None,
            id="cest error"
        ),
        pytest.param(
            [127, 219, 299, 277, 309],
            576,
            (299, 277),
            id="kk"
        ),
    ]
)
def test_find_elements(numbers : list, target_sum : int, expected_elements : tuple) -> None:
    assert expected_elements == find_elements(numbers, target_sum)


@pytest.mark.parametrize(
    "numbers,expected_error",
    [
        pytest.param(
            [
                35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 
                150, 182, 127, 219,
            ],
            127,
            id="example 1",
        ),
    ]
)
def test_find_error(numbers : list, expected_error : int) -> None:
    assert expected_error == find_error(numbers, preamble_len=5)


@pytest.mark.parametrize(
    "numbers,error,expected_sequence",
    [
        pytest.param(
            [
                35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 
                150, 182, 127, 219,
            ],
            127,
            [15, 25, 47, 40],
            id="example 1",
        ),
    ]
)
def test_find_error_elements(numbers : list, error : int, expected_sequence : list) -> None:
    assert expected_sequence == find_error_elements(numbers, error)