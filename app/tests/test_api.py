import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_calculate_carbon():
    payload = {
        "electricity_kwh": 1000,
        "ac_percentage": 50,
        "petrol_liters": 100
    }
    response = client.post("/api/v1/calculate/carbon", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["total_co2_kg"] == 743.0
    assert "breakdown" in data

def test_calculate_water():
    payload = {
        "water_m3": 10
    }
    response = client.post("/api/v1/calculate/water", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["desalination_co2_kg"] == 42.0
