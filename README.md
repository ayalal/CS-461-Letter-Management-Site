# Letter of Recommendation Management Website

This is a web application written in Python using the Django framework. The purpose of this application is to allow OSU students and faculty to better manage the process of requesting letters of recommendation. It facilitates tasks such as requesting a letter from an instructor, uploading a resume and other documents, scheduling when various letters are due, and receving the final letter.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3 is required to run the server

### Installing

A step by step series of examples that tell you how to get a development environment running

Install Django

```
pip install django
```

From the LetterWebsite directory, run the server

```
python3 manage.py runserver
```

Now in a web browser, go to http://127.0.0.1:8000.

## Deployment

By default, the server runs using a SQLite database for easy development on a local machine. For production use, it is recommended to use a MySQL or MariaDB database. Installing MySQL is out of the scope of this guide. After MySQL is installed, create a user and an empty database for use with this project. Now settings.py in the LetterWebsite directory needs to be modified. In the databases section, remove or comment out the code for the SQLite database, and uncomment the code for the MySQL database. Some modifications to the user, password, and host will need to be made for use with the new database.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used

## Authors

* **Lorenzo Ayala** - [ayalal](https://github.com/ayalal)
* **Johnathan Lee** - [innsensed](https://github.com/innsensed)
* **Scott Waddington** - [waddings](https://github.com/waddings)
* **Matthew Kottre** - [Ordexist](https://github.com/Ordexist)
* **Mingwei Gao** - [gaomin03](https://github.com/gaomin03)
