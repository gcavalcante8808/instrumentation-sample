from app import Session
from models.ProductModel import Product, ProductSchema


class ProductView:
    def __init__(self):
        self.session = Session

    def on_get(self, req, resp, id):
        req.context['result'] = self.session.query(Product).all()

    def on_post():
        pass

    def on_put():
        pass
