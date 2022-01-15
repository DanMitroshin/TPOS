import pandas as pd
from sqlalchemy import create_engine, orm
from dataproduct.data import Base, Product


def check_fill(session):
    print('|>>>>> CHECK ROWS IN DB:')
    rows = list(map(lambda p: f'id {p.id}. [name] {p.name}, [cost] {p.cost}', session.query(Product).all()))
    for row in rows:
        print(row)


def fill_db(session):
    print("|>>>> START READ CSV")
    df = pd.read_csv('dbdata/data.csv')
    print("|>>>> SUCCESS READ CSV")
    
    for id_row, row in df.iterrows():
        # print(row)
        session.add(Product(id=id_row + 1, name=row["name"], cost=row["cost"]))
    session.commit()
    print("|>>>> END FILL DB")


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@database:3306/db')
    session = orm.Session(engine)
    Base.metadata.create_all(engine)
    
    fill_db(session)
    check_fill(session)
    print("|>>>> END OF SERVICE-2")
