
## Run Locally

Browse to project directory and activate script

```bash
  venv\Scripts\activate
```

Create a virtual environment

```bash
  pip install virtualenv
```

pip install Django and other dependencies

```bash
  pip install Django

  asgiref             3.8.1
  crispy-tailwind     1.0.3
  Django              5.1.6
  django-crispy-forms 2.3
  pip                 25.0
  psycopg2-binary     2.9.10
  sqlparse            0.5.3
  tzdata              2025.1
```

Install pgAdmin and PostgerSQL. Modify crm > crm > settings.py as shown below

```bash
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database-name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': '<port>',
    }
}
```

Navigate to crm > crm folder. Make migrations

```bash
  python manage.py makemigrations
```

Run migrations

```bash
  python manage.py migrate
```

Check pgAdmin application and database contents. It should be populated with data from the migrations

Run application and browse http://127.0.0.1:8000/

```bash
  python manage.py runserver
```

