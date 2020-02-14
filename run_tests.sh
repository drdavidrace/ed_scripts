#!/usr/bin/env bash
echo "Running the tests"
tests=("array_test" "unit_test"  "pretty_math_test")
test_dir="./tests"
for t in "${tests[@]}";
do
    pushd .
        cd ${test_dir}
        python -m unittest ${t}
    popd
done