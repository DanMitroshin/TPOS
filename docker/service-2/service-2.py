from sys import stderr

import pandas as pd
from sqlalchemy import create_engine, orm

from dataproduct.data import Base, Product


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@database:3306/db')
    session = orm.Session(engine)
    Base.metadata.create_all(engine)
    print("|>>>> START READ CSV")

    df = pd.read_csv('dbdata/data.csv')
    print("|>>>> SUCCESS READ CSV")
    for id_row, row in df.iterrows():
        print(row)
        product = Product(id=id_row, name= row["name"], cost=row["cost"])
        session.add(product)
    session.commit()

    print('Rows added:')
    for product in session.query(Product).all():
        print(f' - id={product.id}, name="{product.name}", cost={product.cost}')
