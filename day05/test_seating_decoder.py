import pytest
from seating_decoder import decode_seat_data


@pytest.mark.parametrize(
    "encoded_id,expected_id",
    [
        pytest.param(
            "FBFBBFFRLR",
            357,
            id="example 1",
        ),
        pytest.param(
            "BFFFBBFRRR", 
            567, 
            id="example 2"
        ),
        pytest.param(
            "FFFBBBFRRR", 
            119, 
            id="example 3"
        ),
        pytest.param(
            "BBFFBBFRLL", 
            820, 
            id="example 4"
        ),
    ]
)
def test_decode_id(encoded_id : str, expected_id : int) -> None:
    assert expected_id == decode_seat_data(encoded_id)["id"]
