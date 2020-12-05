import pytest
from passport_validator import validate_passport, validate_passport_throughly, format_passport_data


@pytest.mark.parametrize(
    "passport_data,is_valid",
    [
        pytest.param(
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", 
            True, 
            id="all fields present"
        ),
        pytest.param(
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
            False, 
            id="missing hgt"
        ),
        pytest.param(
            """hcl:#ae17e1 iyr:2013
            eyr:2024
            ecl:brn pid:760753108 byr:1931
            hgt:179cm
            """,
            True, 
            id="secret santa with missing cid"
        ),
        pytest.param(
            """hcl:#cfa07d eyr:2025 pid:166559648
            iyr:2011 ecl:brn hgt:59in
            """,
            False, 
            id="missing cid and byr"
        ),
        pytest.param(
            """hcl:#6b5442 ecl:brn iyr:2019
            pid:637485594 hgt:171cm
            eyr:2021 byr:1986
            """,
            True, 
            id="missing cid and byr"
        ),
    ]
)
def test_validate_passport(passport_data : str, is_valid : bool) -> None:
    passport_data = format_passport_data(passport_data)
    assert is_valid == validate_passport(passport_data)


@pytest.mark.parametrize(
    "passport_data,is_valid",
    [
        pytest.param(
            """eyr:1972 cid:100
            hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
            """,
            False, 
            id="invalid pid"
        ),
        pytest.param(
            """iyr:2019
            hcl:#602927 eyr:1967 hgt:170cm
            ecl:grn pid:012533040 byr:1946
            """,
            False, 
            id="invalid eyr"
        ),
        pytest.param(
            """hcl:dab227 iyr:2012
            ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
            """,
            False, 
            id="invalid hcl"
        ),
        pytest.param(
            """hgt:59cm ecl:zzz
            eyr:2038 hcl:74454a iyr:2023
            pid:3556412378 byr:2007
            """,
            False, 
            id="invalid eyr"
        ),
        pytest.param(
            """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
            hcl:#623a2f
            """,
            True, 
            id="valid 1"
        ),
        pytest.param(
            """eyr:2029 ecl:blu cid:129 byr:1989
            iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
            """,
            True, 
            id="valid 2"
        ),
        pytest.param(
            """hcl:#888785
            hgt:164cm byr:2001 iyr:2015 cid:88
            pid:545766238 ecl:hzl
            eyr:2022
            """,
            True, 
            id="valid 3"
        ),
        pytest.param(
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
            True, 
            id="valid 4"
        ),
    ]
)
def test_validate_passport_thouroughly(passport_data : str, is_valid : bool) -> None:
    passport_data = format_passport_data(passport_data)
    assert is_valid == validate_passport_throughly(passport_data)