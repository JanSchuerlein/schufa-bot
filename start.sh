#!/bin/bash

#Starts the bot and activates the local python venv from the repo directory, you can point a cronjob to this script path

SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

cd $SCRIPT_PATH

source .venv/bin/activate
python3 bot.py