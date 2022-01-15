FROM python:3.8

COPY ./service-2 .
COPY ./dataproduct ./dataproduct
COPY ./dbdata ./dbdata
RUN pip install pandas sqlalchemy pymysql
CMD python service-2.py
