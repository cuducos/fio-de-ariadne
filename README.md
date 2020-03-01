# Ariadne

This is a proof-of-concept of a system to scrap and structure data about minors in Brazil. Ariadne requires [Python](https://python.org) 3.7+ and [Pipenv](https://pipenv.readthedocs.io/en/latest/).

## Running

### Install the dependencies

```console
$ pipenv install
```

To use the dependencies installed you need to activate the _virtualenv_ with:

```console
$ pipenv shell
```

(Use `exit` to leave the _virtualenv_.)

### Loading data

These commands need to be run only once. They create the database structure, scrap the data and save it to the database:

```console
$ python manage.py migrate
$ python manage.py crawl
```

You also might need to create an user to access the dashboard:

```console
$ python manage.py createsuperuser
```

## Running

```console
$ python manage.py runserver
```

And access the dashboard at [`localhost:8000`](http://localhost:8000).

## Developing

You can install extra dependencies with:
```consle
$ pip install --dev
```

And run some checkers with:

```console
$ pipenv run mypy crawler
$ pipenv run black .
```
