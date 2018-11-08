from falcon import testing
from prometheus_client import Counter,REGISTRY

from .app import app

import json
import pytest

headers = {'Content-Type', 'application/json'}


@pytest.fixture()
def client():
    return testing.TestClient(app)

def test_get_root(client):
    doc = {'Message': 'Hello World'}

    result = client.simulate_get('/')
    assert result.status_code == 200
    assert result.json == doc

REQS = Counter('homepage_req_total','The Number of Index REQs/get')
def req_counter():
    REQS.inc()


def test_req_counter_instrumentation(client):
    import pdb
    pdb.set_trace()
    before = REQS.get_sample_value('homepage_req_total')
    req_counter()
    after = REQS.get_sample_value('homepage_req_total')
    assert before == after - 1

