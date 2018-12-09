from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,Float
from marshmallow_sqlalchemy import ModelSchema

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    enterprise_id = Column(Integer,nullable=False)
    currency = Column(String,default='us_dollar')


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
