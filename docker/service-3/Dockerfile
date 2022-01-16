FROM python:3.8

COPY ./service-3 .
COPY dataproduct/ ./dataproduct/
RUN pip install sqlalchemy pymysql flask
CMD python -m flask run --host=0.0.0.0 --port=10995
