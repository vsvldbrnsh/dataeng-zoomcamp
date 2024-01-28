FROM python:3.9

RUN pip install pandas pgcli jupyter sqlalchemy psycopg2

WORKDIR /app

COPY data_ingestion.py /app/data_ingestion.py

ENTRYPOINT [ "python", "data_ingestion.py" ]