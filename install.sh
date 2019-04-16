#!/bin/bash

# check if python3 is installed
if !(command -v python3 &>/dev/null); then
	echo python3 is not installed. Please install python3 before running this script.
	exit
fi

# check if pip is installed
if !(command -v pip3 --version &>/dev/null); then
	echo pip is not installed. Please install pip before running this script.
	exit
fi

cd LetterWebsite

# install django
pip3 install -r requirements.txt

python3 manage.py runserver
