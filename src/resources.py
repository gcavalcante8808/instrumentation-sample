from app import Session
from models.ProductModel import Product, ProductSchema


class ProductView:
    schema = ProductSchema(session=Session)

    def __init__(self):
        self.session = Session

    def on_get(self, req, resp, id):
        req.context['result'] = self.session.query(Product).all()

    def on_post():
        pass

    def on_put(self, req, resp, **kwargs):
        data = req.context['json']
        if isinstance(data, Product):
            self.session.add(data)
            response = self.session.commit()
            print(data.id)
        pass
