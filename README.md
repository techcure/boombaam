# [Django Dashboard Light Blue](https://appseed.us/admin-dashboards/django-dashboard-light-blue)

**Open-Source Admin Dashboard** coded in **[Django Framework](https://www.djangoproject.com/)** - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).

### Dashboard Features

- SQLite, Django native ORM
- Modular design
- Session-Based authentication (login, register)
- Forms validation
- UI Kit: **Light Blue Dashboard** (Free Version) by **FlatLogic**

### Deployment Scripts

- **Heroku** - Cloud Application Platform
- **Docker** - execute the app using a sandboxed container
- **Gunicorn** / Nginx - a common used configuration for Django Apps
- **Waitress** - Gunicorn equivalent for Windows.       

### Web App Links

- [Django Dashboard Light Blue](https://appseed.us/admin-dashboards/django-dashboard-light-blue) - product page 
- [Django Dashboard Light Blue](https://django-dashboard-light-blue.appseed.us/login/) - LIVE Demo
- [Django Dashboard Light Blue](https://www.youtube.com/watch?v=vsR9GPxEcNQ) - yTube presentation

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, Lifetime updates and **24/7 LIVE Support** (via [Discord](https://discord.gg/fZC6hup)) 

| [Django Dashboard Argon PRO](https://appseed.us/admin-dashboards/django-dashboard-argon-pro) | [Django Dashboard Black PRO](https://appseed.us/admin-dashboards/django-dashboard-black-pro) | [Django Dashboard Dashkit PRO](https://appseed.us/admin-dashboards/django-dashboard-dashkit-pro) |
| --- | --- | --- |
| [![Django Dashboard Argon PRO](https://raw.githubusercontent.com/app-generator/static/master/products/django-dashboard-argon-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-argon-pro)  | [![Django Dashboard Black PRO](https://raw.githubusercontent.com/app-generator/static/master/products/django-dashboard-black-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-black-pro) | [![Django Dashboard Dashkit PRO](https://raw.githubusercontent.com/app-generator/static/master/products/django-dashboard-dashkit-pro-screen.png)](https://appseed.us/admin-dashboards/django-dashboard-dashkit-pro)

<br />
<br />

![Django Dashboard Light Blue - Open-Source Web App.](https://raw.githubusercontent.com/app-generator/static/master/products/django-dashboard-light-blue-screen.png)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-dashboard-light-blue.git
$ cd django-dashboard-light-blue
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$ 
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port 
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Heroku](https://heroku.com/), [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Heroku](https://heroku.com/) platform

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-dashboard-light-blue.git
$ cd django-dashboard-light-blue
$
$ # Heroku Login
$ heroku login
$
$ # Create the app in Heroku platform
$ heroku create # a random name will be generated by Heroku
$
$ # Disable collect static 
$ heroku config:set DISABLE_COLLECTSTATIC=1
$
$ # Push the source code and trigger the deploy
$ git push heroku master
$
$ # Execute DBSchema Migration
$ heroku run python manage.py makemigrations
$ heroku run python manage.py migrate
$
$ # Visit the deployed app in browser.
$ heroku open
$
$ # Create a superuser
$ heroku run python manage.py createsuperuser
```

<br />

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/django-dashboard-light-blue.git
$ cd django-dashboard-light-blue
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running. 

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```
> Start the app using gunicorn binary

```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.


<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```
> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Support

- Free support via eMail < [support @ appseed.us](https://appseed.us/support) > and **Github** issues tracker
- 24/7 Live Support via [Discord](https://discord.gg/fZC6hup) for paid plans and commercial products.

<br />

## Credits

- [Django Framework](https://www.djangoproject.com/) - Offcial website
- [Django Admin Dashboards](https://appseed.us/admin-dashboards/django) - Open-source and paid admin panels coded in **Django**

<br />

## License

@MIT

<br />

---
[Django Dashboard Light Blue](https://appseed.us/admin-dashboards/django-dashboard-light-blue) - Provided by **AppSeed** [Web App Generator](https://appseed.us/app-generator).
