#!/bin/bash

#This script will automatically install all browser dependencies needed for selenium and the schufa bot to work
#If you've already installed selenium drivers or chrome directly on your system, do not run this script

printf "\n\n\nDownloading and installing the latest stable version of google chrome...\n\n\n"

apt update

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i ./google-chrome-stable_current_amd64.deb
apt install -f -y
rm ./google-chrome-stable_current_amd64.deb

printf '\n\n\nDownloading and installing the latest chromedriver version 114.* (v. 04/2024)...\n\n\n'

wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv ./chromedriver /usr/bin/chromedriver
rm ./LICENSE.chromedriver
chmod +x /usr/bin/chromedriver
rm -r chromedriver_linux64.zip