# Fio de Ariadne

This is a proof-of-concept of a system to scrap and structure data about minors in Brazil. Ariadne requires [Python](https://python.org) 3.7+ and [Poetry](https://python-poetry.org/).

## Running

### Install the dependencies

```console
$ poetry install
```

To use the dependencies installed you need to activate the _virtualenv_ with:

```console
$ poetry shell
```

(Use `exit` to leave the _virtualenv_.)

### Configuring the Django application

Simply run this command and follow the instructions:

```console
$ createnv
```

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

You can run some checks with:

```console
$ mypy crawler
$ black .
```
