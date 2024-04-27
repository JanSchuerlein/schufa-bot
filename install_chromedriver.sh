#!/bin/bash

#This script will automatically install the chrome driver linux64 needed for selenium and the schufa bot to work
#If you've already installed selenium chrome drivers directly on your system, do not run this script

apt update

printf '\n\n\nDownloading and installing the latest chromedriver version 124.* (v. 04/2024)...\n\n\n'

wget https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
mv ./chromedriver-linux64/chromedriver /usr/bin/chromedriver
rm ./chromedriver-linux64/LICENSE.chromedriver
chmod +x /usr/bin/chromedriver
rm -r chromedriver-linux64
rm chromedriver-linux64.zip