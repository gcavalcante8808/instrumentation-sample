from app import Session
from prometheus_client import generate_latest
from models.ProductModel import Product, ProductSchema
from falcon import falcon


class ProductView:
    schema = ProductSchema(session=Session)

    def __init__(self):
        self.session = Session

    def on_get(self, req, resp, product_id=None):
        """ List or Retrieve Operation """
        if not product_id:
            self.schema = ProductSchema(session=Session,many=True)
            result = self.session.query(Product).all()
            req.context['result'] = result

        if product_id:
            result = self.session.query(Product).filter_by(id=product_id).first()
            req.context['result'] = result

    def on_post(self, req, resp):
        """ Create Operation """
        data = req.context['json']
        if isinstance(data, Product):
            self.session.add(data)
            self.session.commit()
            resp.status = falcon.HTTP_201

    def on_put(self, req, resp, **kwargs):
        """ Update a specific Object """
        data = req.context['json']
        if isinstance(data, Product):
            self.session.add(data)
            self.session.commit()


class MetricsView:

    def on_get(self, req, resp):
        data = generate_latest()
        resp.content_type = 'text/plain; version=0.0.4; charset=utf-8'
        resp.body = str(data.decode('utf-8'))        
