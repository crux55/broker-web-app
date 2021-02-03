import requests

json = {
    "symbol":"NZD/USD",
    "amount":7,
    "stop": -3.5,
    "limit": 14,
    "trailing": ".5",
    "flipping": True,
    "allow_multi": True
}


def test_object_definition():
    response = requests.post("http://localhost:8080/objecttest", json=json)
    assert response.status_code == 200


def test_create_long():
    response = requests.post("http://localhost:8080/buy", json=json)
    assert response.status_code == 200
    response = requests.get("http://localhost:8080/close",{'id': response.content.decode(), 'amount': json.get('amount')})
    assert response.status_code == 200


def test_create_short():
    response = requests.post("http://localhost:8080/sell", json=json)
    assert response.status_code == 200
    response = requests.get("http://localhost:8080/close",{'id': response.content.decode(), 'amount': json.get('amount')})
    assert response.status_code == 200
