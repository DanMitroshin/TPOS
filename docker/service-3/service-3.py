from sqlalchemy import create_engine, orm

from flask import Flask, request
from dataproduct.data import Product


app = Flask(__name__)
engine = create_engine('mysql+pymysql://root:@database:3306/db', pool_recycle=3600)
session = orm.Session(engine)


@app.errorhandler(404)
def page_not_found(e):
    return 'Not found. Error 404\n', 404


@app.route('/health')
def health():
    return 'ok\n', 200


@app.route('/')
def handler():
    id_product = request.args.get('id')
    if id_product is None:
        return "Not provide product id", 500
    product = session.query(Product).get({'id': id_product})
    if product is None:
        return "Unreal product id", 500
    return f"Product: {product.name} - {product.cost} RUB\n", 200
