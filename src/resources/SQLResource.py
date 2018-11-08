from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from marshmallow_sqlalchemy import ModelSchema

class SQLResource:
    def __init__(self, session: scoped_session, 
                 resource: declarative_base, 
                 schema: ModelSchema):
        self.session = session
        self.resource = resource
        # self.schema = schema

    """ Index Route """
    def on_get(self, req, resp):
        req.context['result'] = self.session.query(self.resource).all()
