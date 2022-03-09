#!/usr/bin/env bash

# exit if error
set -e

./check_type_hints.sh

cd ./tests

./run_tests.sh

