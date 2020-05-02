FROM python:3.7-slim

WORKDIR /fio/
COPY pyproject.toml .
COPY poetry.lock .

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install

COPY manage.py manage.py
COPY scrapy.cfg scrapy.cfg
COPY setup.cfg setup.cfg

COPY crawler/ crawler/
COPY web/ web/

ENTRYPOINT ["poetry", "run"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
