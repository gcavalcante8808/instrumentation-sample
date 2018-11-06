from falcon import testing

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