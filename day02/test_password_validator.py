import pytest
from password_validator import validate_password, validate_password_method_2

@pytest.mark.parametrize(
    "policy,password,is_valid",
    [
        pytest.param("1-3 a", "abcde", True, id="at bottom range"),
        pytest.param("2-9 c", "ccccccccc", True, id="at top range"),
        pytest.param("2-3 b", "", False, id="empty"),
        pytest.param("9-10 e", "abcde", False, id="under bottom range"),
        pytest.param("2-3 f", "zbfmafofp1fasdf", False, id="over top range"),
    ]
)
def test_validate_password(policy : str, password : str, is_valid : bool) -> None:
    assert is_valid == validate_password(policy, password)


@pytest.mark.parametrize(
    "policy,password,is_valid",
    [
        pytest.param("1-3 a", "abcde", True, id="one match"),
        pytest.param("1-3 b", "cdefg", False, id="no matches"),
        pytest.param("2-9 c", "ccccccccc", False, id="multiple matches"),
    ]
)
def test_validate_password_method_2(policy : str, password : str, is_valid : bool) -> None:
    assert is_valid == validate_password_method_2(policy, password)
