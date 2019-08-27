
import json
import pytest
from webapp.backend import create_app

app = create_app("testing")


@pytest.fixture
def client(request):
    test_client = app.test_client()
    return test_client


def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type="application/json")


def decode_response(response):
    return json.loads(response.data.decode("utf8"))


def test_predict_endpoint(client):
    response = post_json(client, "/api/predict", {})
    assert response.status_code == 200
    assert decode_response(response) == {"predict_value": [120.23]}
