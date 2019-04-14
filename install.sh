#!/bin/bash

# check if python3 is installed
if !(command -v python3 &>/dev/null); then
	echo python3 is not installed. Please install python3 before running this script.
	exit
fi

cd LetterWebsite

# install django
pip3 install django

python3 manage.py runserver
