from flask import Flask, request, jsonify
from sqlalchemy import create_engine, orm
from dataproduct.data import Product


app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:@database:10994/products_db')
session = orm.Session(engine)


@app.route('/health')
def get_health():
    return '200\n', 200


@app.errorhandler(404)
def not_found():
    return 'Not found. Error 404\n', 404


def product_to_dict(p):
    return {
        'id': p.id,
        'name': p.name,
        'cost': p.cost,
    }


@app.route('/all')
def get_all_products():
    queryset = session.query(Product).all()
    products = list(map(product_to_dict, queryset))
    return jsonify(products)


@app.route('/')
def get_product():
    id_product = request.args.get('id')
    if id_product is None:
        return "Id is required\n", 500
    product = session.query(Product).get({'id': id_product})
    if product is None:
        return "Unreal product id\n", 500
    return jsonify(product_to_dict(product))
