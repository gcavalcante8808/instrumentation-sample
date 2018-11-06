

from werkzeug.serving import run_simple


import falcon
import json

app = falcon.API(media_type='application/json')

class DefaultResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({"Message":"Hello World"})
        resp.status_code = 200

resources = DefaultResource()
app.add_route('/', resources)


if __name__ == '__main__':
    run_simple('localhost',5000, app, use_reloader=True)