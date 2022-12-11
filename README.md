
# KURULUM

cd .. 

**mkdir home/Desktop/rest_app**

**cd home/Desktop/rest_app**

python3 -m venv env
>source env/bin/activate
>```git clone https://github.com/mertcaliskanlnx/rest_framework-django.git```

###### python3 -r requipment.txt

```
django-project-klasor/
├── env
```

source /env/bin/activate
> django-admin startproject haberbulteni .
```

haberbulteni/
├── asgi.py
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-310.pyc
│   ├── settings.cpython-310.pyc
│   ├── urls.cpython-310.pyc
│   └── wsgi.cpython-310.pyc
├── settings.py
├── urls.py
└── wsgi.py
├── env
```

> python3 manage.py startapp haberler

```
haberler/
├── admin.py
├── api
│   ├── __pycache__
│   │   ├── serializers.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── apps.py
├── __init__.py
├── models.py
├── __pycache__
│   ├── admin.cpython-310.pyc
│   ├── apps.cpython-310.pyc
│   ├── __init__.cpython-310.pyc
│   └── models.cpython-310.pyc
├── tests.py
└── views.py
```
```
├── manage.py
├── README.md
├── LICENSE.md
├── requipment.txt
├── db_sqlite3.sql
├── env

```
```
kitaplar/
├── admin.py
├── api
│   ├── pagination.py
│   ├── permission.py
│   ├── __pycache__
│   │   ├── pagination.cpython-310.pyc
│   │   ├── permission.cpython-310.pyc
│   │   ├── serializers.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── apps.py
├── __init__.py
├── migrations
│   ├── 0001_initial.py
│   ├── 0002_alter_yorum_yorum_sahibi.py
│   ├── __init__.py
│   └── __pycache__
│       ├── 0001_initial.cpython-310.pyc
│       ├── 0002_alter_yorum_yorum_sahibi.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── models.py
├── __pycache__
│   ├── admin.cpython-310.pyc
│   ├── apps.cpython-310.pyc
│   ├── __init__.cpython-310.pyc
│   └── models.cpython-310.pyc
├── tests.py
└── views.py
```
```
scripts/
├── fake_data.py
├── __init__.py
└── __pycache__
    ├── fake_data.cpython-310.pyc
    └── __init__.cpython-310.pyc


```
**python3 manage.py runserver**
>http://127.0.0.1:8000/api_kitaplar/kitaplar/
