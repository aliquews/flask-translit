FROM python:3.10

WORKDIR /flask-app

COPY ./requirements.txt /flask-app/requirements.txt
COPY ./migrations /flask-app/migrations
COPY ./alembic.ini /flask-app/alembic.ini
COPY ./config.py /flask-app/config.py
COPY ./src /flask-app/src

ENV DB_URL="postgresql+psycopg2://postgres:postgres@pgdb/postgres"

RUN pip install --no-cache-dir --upgrade -r requirements.txt


ENTRYPOINT [ "python" ]
CMD ["src/main.py"]