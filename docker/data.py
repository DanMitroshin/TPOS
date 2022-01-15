from sqlalchemy import Integer, Text, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    cost = Column(Integer, nullable=False)
