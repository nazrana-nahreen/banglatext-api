
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_process_bengali_text():
    response = client.post(
        "/process",
        json={"text": "আমি বাংলা শিখি। তুমি কি শিখো?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["cleaned_text"] == "আমি বাংলা শিখি। তুমি কি শিখো?"
    assert data["statistics"]["words"] == 6
    assert data["statistics"]["sentences"] == 2


def test_extra_spaces_are_removed():
    response = client.post(
        "/process",
        json={"text": "  আমি   বাংলা  শিখি  "}
    )

    assert response.status_code == 200
    assert response.json()["cleaned_text"] == "আমি বাংলা শিখি"

def test_process_english_sentences():
    response = client.post(
        "/process",
        json={"text": "I am fine. How are you?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["statistics"]["sentences"] == 2

def test_sentiment_positive():
    response = client.post(
        "/sentiment",
        json={"text": "এই পণ্যটির মান খুব ভালো, আমি সন্তুষ্ট।"},
    )

    assert response.status_code == 200

    data = response.json()
    assert data["sentiment"] == "positive"
    assert 0 <= data["model_score"] <= 1


def test_sentiment_empty_text():
    response = client.post(
        "/sentiment",
        json={"text": ""},
    )

    assert response.status_code == 422
