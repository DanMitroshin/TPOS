from sqlalchemy import create_engine, orm

from flask import Flask, request, abort
from dataproduct.data import Product


app = Flask(__name__)
engine = create_engine('mysql+pymysql://root:@database:3306/db', pool_recycle=3600)
session = orm.Session(engine)


@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found. Error 404\n', 404


@app.route('/health')
def health():
    return 'ok\n', 200


@app.route('/')
def handler():
    try:
        id_product = request.args.get('id')
        if id_product is None:
            abort(404)
        product = session.query(Product).get({'id': id_product})
        if region is None:
            abort(404)
        return f"Product: {product.name} - {product.cost} RUB\n", 200
    except Exception as e:
        return f"ERROR: {e}\n", 200
