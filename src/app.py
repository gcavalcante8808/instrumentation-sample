from werkzeug.serving import run_simple


import falcon
import json


#Middlewares
from falcon_marshmallow import Marshmallow
from middleware.PrometheusMiddleware import PrometheusMiddleware
from middleware.SQLAlchemyMiddleware import SQLAlchemySessionManager

#Models and Schemas
from models.ProductModel import Base, Product, ProductSchema
from resources.SQLResource import SQLResource


from utils.db import setup_db


#Marshmallow serialize/deserialize framework.
marshmallow = Marshmallow()

#Initialize App and ADD prometheus middleware.
prometheus = PrometheusMiddleware()

#setup Db.
Session = setup_db(Base)
sqlalchemy = SQLAlchemySessionManager(Session)

app = falcon.API(middleware=[
                 
                 prometheus,
                 sqlalchemy,
                 marshmallow,
])

app.add_route('/metrics', prometheus)


#Product Endpoint
product_resource = SQLResource(Session, Product, ProductSchema)
app.add_route('/products', product_resource)


if __name__ == '__main__':
    run_simple('localhost',5000, app, use_reloader=True)
