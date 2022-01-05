### Create a virtual env

virtualenv venv

### Activate a virtual env

source venv/bin/activate

### Deactivate a virtual env

virtualenv venv

### Install Django and DRF (Django Rest Framework)

pip install djangorestframework


### Start the admin aplication

django-admin startproject name_admin_aplication

### Start normal aplication

django-admin startapp name_aplication


### Project structure

```
.
├── README.md                # README file
├── ecommerce_rest
|   ├── settings             # New Django settings folder
│   |   ├── base.py          # Normal settings
│   |   ├── local.py         # Specific local development settings
│   |   └── production.py    # Specific production settings
|   ├── __init__.py          
|   ├── asgi.py              
|   ├── urls.py              
|   └── wsgi.py              
├── manage.py
├── venv                     # Virtual enviroment folder
└── .gitignore.json          # files to ignore

```

### Generate requirements.txt file

pip freeze > requirements.txt


### Create a super user for django admin

python manage.py createsuperuser

### Document the API with OpenAPI

install 

pip install drf-spectacular

You see (dev):

http://localhost:8000/api/schema/swagger-ui/

http://localhost:8000/api/schema/redoc/