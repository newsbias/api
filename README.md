# NewsBias API

**QUICKSTART:** To run the application with Docker, ensure you have
`docker-compose` installed and simply run:

```sh
$ ./doit up
$ ./doit python manage.py migrate
```

and open your web browser to `http://localhost:8000`.

## Non-Docker workflow

To get set up, first install [`pipenv`](https://github.com/pypa/pipenv). This
can be done easily with:

```sh
$ pip3 install --user pipenv
```

assuming you have Python 3 installed.

Once you have `pipenv`, run

```sh
$ pipenv install
```

to create and install the virtual environment, then

```sh
$ pipenv run python manage.py --help
```

to see all possible `manage.py` commands. The most useful one, which runs a
development server, is:

```sh
$ pipenv run python manage.py runserver
```

which starts a server accessible at `http://localhost:8000`.
