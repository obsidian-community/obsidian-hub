#!/usr/bin/env bash

# exit if error
set -e


# check that in scripts directory

CURRENT_DIR="$(pwd)"
SCRIPTS_DIR='obsidian-hub/.github/scripts'

if ! [[ "$CURRENT_DIR" =~ "$SCRIPTS_DIR" ]] ; then
    echo "Your current directory is $CURRENT_DIR"
    echo "It needs to be ...$SCRIPTS_DIR"
    exit 1
fi


# check if virtual environment is activated

PYTHON="$(which python)"
PARTIAL_PATH='venv/bin/python'

if ! [[ "$PYTHON" =~ "$PARTIAL_PATH" ]] ; then
    echo 'The virtual environment is not active. Type the following to activate it:'
    # Sourcing only works in interactive shells
    # This is why it cannot be done by script
    echo 'source ./../../venv/bin/activate'
    exit 1
fi


# tests

./check_type_hints.sh

cd ./tests

./run_tests.sh

