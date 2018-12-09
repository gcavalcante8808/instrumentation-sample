from werkzeug.serving import run_simple


import falcon

#Middlewares

from falcon_openapi import OpenApiRouter
from falcon_marshmallow import Marshmallow as MarshmallowMiddleware
from middleware.PrometheusMiddlewares import RequestsCounterMiddleware, RequestsTimerMiddleware
from middleware.SQLAlchemyMiddleware import SQLAlchemySessionManager

# #Models and Schemas
from models.ProductModel import Base
from utils.db import setup_db


#Marshmallow serialize/deserialize framework Middleware.
marshmallow = MarshmallowMiddleware()

#Initialize App and ADD prometheus middleware.
req_counter = RequestsCounterMiddleware()
req_timer = RequestsTimerMiddleware()

#setup Db. Strip base from ProductModel.
Session = setup_db(Base)
sqlalchemy = SQLAlchemySessionManager(Session)

router = OpenApiRouter(file_path='specs/product.yml')
app = falcon.API(middleware=[
                 req_timer,
                 req_counter,
                 sqlalchemy,
                 marshmallow,
                ],
                router=router
)

if __name__ == '__main__':
    run_simple('0.0.0.0',5000, app, use_reloader=True, use_debugger=True)
