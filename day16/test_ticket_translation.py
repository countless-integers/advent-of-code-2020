import pytest
from ticket_translation import TicketValidator
from typing import List


@pytest.mark.parametrize(
    ["rules"],
    [
        pytest.param(
            [
                "class: 1-3 or 5-7",
                "row: 6-11 or 33-44",
                "seat: 13-40 or 45-50",
            ],
        )
    ]
)
@pytest.mark.parametrize(
    ["values", "expected_result"],
    [
        pytest.param([7,1,14], [], id="example 1"),
        pytest.param([7,3,47], [], id="example 2"),
        pytest.param([40,4,50], [4], id="example 3"),
        pytest.param([55,2,20], [55], id="example 4"),
        pytest.param([38,6,12], [12], id="example 5"),
    ]
)
def test_method(values : str, rules : List[str], expected_result : bool) -> None:
    validator = TicketValidator()
    validator.addRules(rules)
    result = validator.validate_all(values)
    assert expected_result == result["invalid_values"]
