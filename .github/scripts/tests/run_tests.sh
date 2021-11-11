#!/usr/bin/env sh

cd ..
# -s means "show console output if test fails"
python3 -s -m pytest tests
