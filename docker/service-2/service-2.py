from sys import stderr

import pandas as pd
from sqlalchemy import create_engine, orm

from dataproduct.data import Base, Product

def check_fill():
    print('|>>>>> CHECK ROWS IN DB:')
    rows = list(map(lambda p: f'id {p.id}. [name] {p.name}, [cost] {p.cost}', session.query(Product).all()))
    for row in rows:
        print(row)
#     for product in session.query(Product).all():
#         print(f'id={product.id}. name="{product.name}", cost={product.cost}')

def fill_db():
    engine = create_engine('mysql+pymysql://root:@database:3306/db')
    session = orm.Session(engine)
    Base.metadata.create_all(engine)
    print("|>>>> START READ CSV")

    df = pd.read_csv('dbdata/data.csv')
    print("|>>>> SUCCESS READ CSV")
    for id_row, row in df.iterrows():
        # print(row)
        product = Product(id=id_row + 1, name=row["name"], cost=row["cost"])
        session.add(product)
    session.commit()
    print("|>>>> END FILL")

if __name__ == '__main__':
    fill_db()
    check_fill()
