import json
from lambda_function import lambda_handler

def test_lambda_handler():
    event = {"name": "Sivapriya"}

    response = lambda_handler(event, None)
    body = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert body["message"] == "Hello, Sivapriya!"
    assert body["status"] == "success"

def test_default_name():
    response = lambda_handler({}, None)
    body = json.loads(response["body"])

    assert body["message"] == "Hello, World!"
