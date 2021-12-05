# django-first
The first project of dJango

## Set up the project with Virtual Envirenment

#### Create virtual env
`mkdir django-first`
`cd django-first`
`virtualenv venv -p python3`

### Activate virtula env
`source venv/bin/activate`

### Deactive virual env
`deactivate`

### Install Django inside venv
`pip install Django`

### Create requirement file
`pip freeze > requirements.txt`

### Create your project
`django-admin startproject djcrm .`

### Migration
`python manage.py migrate`

### Create tables on DB
`python manage.py makemigrations`

### Run django app
`python manage.py runserver`

### Create new django app
`python manage.py startapp leeds`

### django shell
`python manage.py shell`

### Create super user
`python manage.py createsuperuser`
    name: `admin`
    email: `admin@admin.com`,
    pwd: `123456789`