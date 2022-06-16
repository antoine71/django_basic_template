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
You'll be prompted for the project name, if you wish to use postgresql and DRF. Provide the information, then a Django project will be created for you. Enter the project and take a look around :
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
Rename the file `config/settings/.env_rename_me` to `config/settings/.env` and change the variables values to whatever parameter suits your local configuration.
```
mv config/settings/.env_rename_me config/settings/.env
nano config/settings/.env

SECRET_KEY=<your local secretkey>
DATABASE_NAME=<your database namey>
DATABASE_USER=<your database username>
DATABASE_PASSWORD=<your database password>
DATABASE_HOST=localhost
DATABASE_PORT=5432
ADMIN_URL=admin/
```
The project contains a module 'sample_app'. You can keep it, explore it and modify it as requiredd to suit your needs or simply delete it and create a brand new app with the command 
```
python manage.py startapp <your_app_name>
```
Dont'forget to register your app in the `INSTALLED_APPS` list in the settings file `./config/settings/base.py`

Create a git repo and push it there :
```
git init
git add -A
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:antoine_71/my_project_name.git
git push -u origin main
```

Create the migrations, push it to the database, create a superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Run the development server
```
python manage.py runserver
```