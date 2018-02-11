FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.6.0

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN pip install pipenv

RUN mkdir /app
WORKDIR /app
ADD Pipfile /app/
ADD Pipfile.lock /app/

RUN pipenv install
ADD . /app
ENTRYPOINT [ "/usr/local/bin/pipenv", "run" ]
CMD [ "gunicorn", "api.wsgi.application", "-w", "2", "-b", "0.0.0.0:8000" ]
