#!/bin/bash

SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd $SCRIPT_PATH

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt