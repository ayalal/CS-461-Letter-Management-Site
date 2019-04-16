# Letter of Recommendation Management Website

This is a web application written in Python using the Django framework. The purpose of this application is to allow OSU students and faculty to better manage the process of requesting letters of recommendation. It facilitates tasks such as requesting a letter from an instructor, uploading a resume and other documents, scheduling when various letters are due, and receving the final letter.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3 is required to run the server

### Installing

A step by step series of examples that tell you how to get a development environment running

First install Python 3.7 at this website https://www.python.org/downloads/ pip3 should also be installed with the download if 
not install pip3

Then where our project is go to the directory containing the install.sh file and run the code below. (this is for Linux/MacOS machines)
Running this application within Linux context would be the best suited environment. 

```
./install.sh
```

The application should launch and can be used with the credentials below.


Now in a web browser, go to http://127.0.0.1:8000.

If you're still having trouble installing Django, you can always refer to Django's official documentation [here](https://docs.djangoproject.com/en/2.1/topics/install/#install-the-django-code) for more help.

## Deployment

By default, the server runs using a SQLite database for easy development on a local machine. For production use, it is recommended to use a MySQL or MariaDB database. Installing MySQL is out of the scope of this guide. After MySQL is installed, create a user and an empty database for use with this project. Now settings.py in the LetterWebsite directory needs to be modified. In the databases section, remove or comment out the code for the SQLite database, and uncomment the code for the MySQL database. Some modifications to the user, password, and host will need to be made for use with the new database.

### URLs

Most of the URLs for our project are not yet accessible via buttons or links, and so the URLs must be manually typed into the browser's URL bar. Below are the URLs which are accessible for our site:

* **/** (the homepage, also where students can upload their documents and view their requests.)
* **/login** (the login page)
* **/register** (user registration page)
* **/logout** (user logout page)
* **/student_profiles/<user_id>** (student's profile page. A student account can view only their own student profile. Professor accounts can view any student account. If the given id corresponds to a professor's account, the user is redirected to the professor_profiles page instead)
* **/professor_profiles/<user_id>** (professor's profile page. Any student csan view any professor's page. If the user id entered is not a professor account, a 404 error is raised)
* **/preferences** (only accessible by professor accounts. A professor can set their own preferences here. Students who try to access this page are prompted to login as a professor account)
* **/schedule** (This page is hardcoded and not working properly at the moment. Students should be able to view their active requests here. Instead, student's can view their active requests in the index page)

From any URL, the student can initiate a request to a professor by typing their username in the search box and clicking the request button. They **MUST** request to a valid professor username or the webpage will return an error


## Notes

There are some premade accounts to login and test the website's functionality with. Their information is:

* **teacher//testpass123** 
* **student//somepassword**

Make sure to be signed out of the current account before signing in to any other account because that will cause unexpected errors that won't be present with a CAS implementation. These premade accounts are already assigned to a professor group and student group respectively which is important because that is how the website determines if you're a student or professor. New accounts are not assigned to a group and must be manually done.


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used

## Authors

* **Lorenzo Ayala** - [ayalal](https://github.com/ayalal)
* **Johnathan Lee** - [innsensed](https://github.com/innsensed)
* **Scott Waddington** - [waddings](https://github.com/waddings)
* **Matthew Kottre** - [Ordexist](https://github.com/Ordexist)
* **Mingwei Gao** - [gaomin03](https://github.com/gaomin03)
