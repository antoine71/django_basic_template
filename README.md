# Django Basic Template
**A very basic Cookiecutter Django project template**

This is a very basic Django template aimed to replace the command `django-admin startproject`. This template follows the directory structure recommended in Two Scoops of Django by [Daniel & Audrey Roy Greenfeld](https://daniel.roygreenfeld.com/).

## Version
This is an alpha version aimed to be fine tuned.

## Usage

Rather than using `startproject`, get [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work:
```
pip install cookiecutter
```

Now run it against this repo :
```
cookiecutter https://github.com/antoine71/django_basic_template
```

You'll be prompted for the project name and if you wish to use DRF. Provide the information, then a Django project will be created for you. Enter the project and take a look around :
```
cd my_project_name/
ls
```

Create a virtual environnement :
```
python -m venv env
source env/bin/activate
pip install -r requirements/local.txt
```

Or with [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/) :
```
mkvirtualenv my_project_name
```

Install the dependencies :
```
pip install -r requirements/local.txt
```

Create a git repo and push it there :
```
git init
git add -A
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:antoine_71/my_project_name.git
git push -u origin main
```
