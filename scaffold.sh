#!/bin/bash

if [ -z $1 ] || [ -z $2 ]; then
    echo "you need to provide 2 positional arguments: <day number> <module_name>"
    exit 2
fi

dir="day$(printf '%02d' $1)"
mkdir $dir
touch $dir/$2.py
touch $dir/test_$2.py
touch $dir/input.txt

cat > $dir/test_$2.py <<CONTENT
import pytest
from $2 import method


@pytest.mark.parametrize(
    ["value", "expected_value"],
    [
        pytest.param(
            11,
            73,
            id="example 1",
        ),
    ]
)
def test_method(value : int, expected_value : int) -> None:
    assert expected_value == method(mask, value)
CONTENT

cat > $dir/$2.py <<CONTENT
from os.path import dirname, realpath


def method():
    pass


if __name__ == "__main__":
    dir_path = dirname(realpath(__file__))
    with open(dir_path + "/input.txt") as input_file:
        pass
CONTENT