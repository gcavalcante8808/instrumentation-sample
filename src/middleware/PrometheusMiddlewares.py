#Based on: https://gitlab.com/shdh/falcon-prometheus/raw/master/falcon_prometheus/middleware.py

from prometheus_client import CollectorRegistry, Counter, Histogram
import time

request_counter = Counter(
    'app_requests_count',
    'Counter of total HTTP requests',
    ['method', 'path', 'status', 'enterprise_id']
)

request_timer = Histogram(
    'app_requests_elapsed',
    'Histogram of elapsed time in second for requests.',
    ['method', 'path', 'status', 'enterprise_id']
)


class RequestsCounterMiddleware(object):
    """ Count resquests by method, path and status """

    def process_response(self, req, resp, resource, req_succeeded):
        request_counter.labels(method=req.method,
                               path=req.path,
                               status=resp.status,
                               enterprise_id=req.context['Enterprise-Id']).inc()


class RequestsTimerMiddleware(object):
    """ Observe elapsed seconds by each request """
    def process_request(self, req, resp):
        req.start_time = time.time()

    def process_response(self, req, resp, resource, req_succeeded):
        resp_time = time.time() - req.start_time
        request_timer.labels(method=req.method,
                             path=req.path,
                             status=resp.status,
                             enterprise_id=req.context['Enterprise-Id']).observe(resp_time)
