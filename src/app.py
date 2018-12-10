from werkzeug.serving import run_simple


import falcon

#Middlewares

from falcon_openapi import OpenApiRouter
from falcon_marshmallow import Marshmallow as MarshmallowMiddleware
from middleware.PrometheusMiddlewares import RequestsCounterMiddleware, RequestsTimerMiddleware
from middleware.SQLAlchemyMiddleware import SQLAlchemySessionManager
from middleware.RequestOwnerMiddleware import InjectOwnerIntoContextMiddleware

# #Models and Schemas
from models.ProductModel import Base
from utils.db import setup_db


#setup Db. Strip base from ProductModel.
Session = setup_db(Base)
sqlalchemy = SQLAlchemySessionManager(Session)

router = OpenApiRouter(file_path='specs/product.yml')
app = falcon.API(middleware=[
                 InjectOwnerIntoContextMiddleware(),
                 RequestsTimerMiddleware(),
                 RequestsCounterMiddleware(),
                 MarshmallowMiddleware(),
                 sqlalchemy,
                ],
                router=router
)

if __name__ == '__main__':
    run_simple('0.0.0.0',5000, app, use_reloader=True, use_debugger=True)
