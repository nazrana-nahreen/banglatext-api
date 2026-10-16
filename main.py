
import re
import unicodedata
from transformers import pipeline

from fastapi import FastAPI
from pydantic import BaseModel, Field

# Load the AI model once when the API starts
sentiment_classifier = pipeline(
    "text-classification",
    model="gradienninja/bangla-sentiment-analyzer",
    device=-1,
)

SENTIMENT_LABELS = {
    "LABEL_0": "negative",
    "LABEL_1": "positive",
    "LABEL_2": "neutral",
}

app = FastAPI(
    title="BanglaText API",
    description="A simple API for processing Bengali text.",
    version="0.1.0",
)


class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=10000)


@app.get("/")
def home():
    return {
        "message": "Welcome to BanglaText API!",
        "status": "running",
    }


@app.post("/process")
def process_text(request: TextRequest):
    # 1. Normalize Unicode representation
    normalized = unicodedata.normalize("NFC", request.text)

    # 2. Remove extra spaces and newlines
    cleaned = re.sub(r"\s+", " ", normalized).strip()

    # 3. Count words (whitespace-separated tokens)
    words = cleaned.split() if cleaned else []

    # 4. Count sentences using common punctuation
    sentences = [
        s for s in re.split(r"[।.!?]+", cleaned) if s.strip()
    ]

    return {
        "original_text": request.text,
        "cleaned_text": cleaned,
        "statistics": {
            "characters": len(cleaned),
            "words": len(words),
            "sentences": len(sentences),
        },
    }

@app.post("/sentiment")
def analyze_sentiment(request: TextRequest):
    result = sentiment_classifier(request.text)[0]

    return {
        "text": request.text,
        "sentiment": SENTIMENT_LABELS.get(
            result["label"], "unknown"
        ),
        "model_score": round(result["score"], 4),
        "note": "AI prediction; results may be incorrect.",
    }