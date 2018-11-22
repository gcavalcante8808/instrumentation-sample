from app import Session
from models.ProductModel import Product, ProductSchema
from falcon import falcon


class ProductView:
    schema = ProductSchema(session=Session)

    def __init__(self):
        self.session = Session

    def on_get(self, req, resp, product_id=None):
        """ List or Retrieve Operation """
        if not product_id:
            req.context['result'] = self.session.query(Product).all()

        #Retrieve Operation.
        result = self.session.query(Product).filter_by(id=product_id).first()
        if result:
            req.context['result'] = result
        resp.status = falcon.HTTP_404

    def on_post():
        """ Create Operation """
        pass

    def on_put(self, req, resp, **kwargs):
        data = req.context['json']
        if isinstance(data, Product):
            self.session.add(data)
            self.session.commit()
            
        