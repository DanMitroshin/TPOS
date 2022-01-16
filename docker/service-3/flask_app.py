from flask import Flask, request
from sqlalchemy import create_engine, orm
from dataproduct.data import Product


app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:@database:10994/products_db')
session = orm.Session(engine)


@app.route('/health')
def get_health():
    return 'ok\n', 200


@app.errorhandler(404)
def not_found():
    return 'Not found. Error 404\n', 404


@app.route('/')
def get_product():
    id_product = request.args.get('id')
    if id_product is None:
        return "Not provide product id\n", 500
    product = session.query(Product).get({'id': id_product})
    if product is None:
        return "Unreal product id\n", 500
    return f"Product: {product.name} - {product.cost} RUB\n", 200
