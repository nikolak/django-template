# Introduction

The goal of this project is to provide minimalistic django project template that everyone can use. 
Template is written with django 1.9 and python 3 in mind.

The main features are:

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in as demo

* Procfile for easy deployments

* Separated requirements files

* SQLite by default if no env variable is set

# Usage

To use this template to start your own project simply run:

    django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      <project_name>

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
