#### 1.  Setup Project
```
$ django-admin.py startproject mysite
```

Creates file structure:
```
mysite/
     manage.py
     mysite/
          __init__.py
          settings.py (db, 
          urls.py
          wsgi.py
```



##### Run server

The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

```
$ python manage.py runserver 0.0.0.0:8080
```

#### 2. Start an app 

```
$ python manage.py startapp polls 
```

Creates ‘mysite/polls’ file structure:
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py (Manually created: For routing)
    views.py (Controller code)
```