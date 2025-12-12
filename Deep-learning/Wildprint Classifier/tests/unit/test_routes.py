# Ce test vérifie que les pages principales se chargent bien (code 200).

from fastapi.testclient import TestClient
from app.API.app import app

client = TestClient(app)

def test_home_route():
    response = client.get("/")
    assert response.status_code == 200

def test_scan_route():
    response = client.get("/scan")
    assert response.status_code == 200

def test_mentions_legales_route():
    response = client.get("/mentions_legales")
    assert response.status_code == 200
