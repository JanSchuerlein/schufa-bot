#!/bin/bash

#This script will automatically install google chrome amd64 needed for selenium, the chrome driver and the schufa bot to work
#If you've already installed google chrome directly on your system, do not run this script

printf "\n\n\nDownloading and installing the latest stable version of google chrome...\n\n\n"

apt update

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i ./google-chrome-stable_current_amd64.deb
apt install -f -y
rm ./google-chrome-stable_current_amd64.deb