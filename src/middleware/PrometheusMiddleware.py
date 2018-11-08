#Based on: https://gitlab.com/shdh/falcon-prometheus/raw/master/falcon_prometheus/middleware.py

from prometheus_client import CollectorRegistry, Counter, Histogram, generate_latest
import time


class PrometheusMiddleware(object):
    def __init__(self):
        self.registry = CollectorRegistry()
        self.requests = Counter(
            'http_total_request',
            'Counter of total HTTP requests',
            ['method', 'path', 'status'],
            registry=self.registry)

    def process_request(self, req, resp):
        req.start_time = time.time()

    def process_response(self, req, resp, resource, req_succeeded):
        resp_time = time.time() - req.start_time

        self.requests.labels(method=req.method, path=req.path, status=resp.status).inc()

    def on_get(self, req, resp):
        data = generate_latest(self.registry)
        resp.content_type = 'text/plain; version=0.0.4; charset=utf-8'
        resp.body = str(data.decode('utf-8'))