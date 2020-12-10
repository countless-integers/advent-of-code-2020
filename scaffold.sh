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