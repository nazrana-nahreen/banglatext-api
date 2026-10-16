# BanglaText API 🇧🇩

**An AI-powered Bengali text processing and sentiment analysis API built with FastAPI and Transformers.**

BanglaText API provides a simple REST API for processing Bengali and mixed-language text. It includes text cleaning, basic text statistics, and AI-powered sentiment analysis using a pretrained Bengali language model.

## ✨ Features

- **Text Processing:** Normalize Unicode text and remove extra whitespace.
- **Text Statistics:** Count characters, words, and sentences.
- **Sentiment Analysis:** Predict positive, negative, or neutral sentiment for text.
- **Input Validation:** Validate request text length using Pydantic.
- **Interactive API Documentation:** Explore and test endpoints using Swagger UI.
- **Automated Testing:** Test API functionality using Pytest.

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Hugging Face Transformers
- PyTorch
- Pytest
- HTTPX
- Uvicorn

## 📁 Project Structure

```text
banglatext-api/
├── main.py
├── test_ai_model.py
├── requirements.txt
├── render.yaml
├── Procfile
├── .python-version
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
└── tests/
    └── test_main.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- Git
- Internet connection for installing dependencies and downloading the pretrained model

### 1. Clone the repository

```bash
git clone https://github.com/nazrana-nahreen/banglatext-api.git
cd banglatext-api
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the API server

```bash
python -m uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

**Note:** The sentiment model downloads pretrained files from Hugging Face when first loaded. Initial startup may take some time and requires sufficient memory and disk space.

## 📌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message and API status |
| GET | `/health` | Health check for deployment monitoring |
| POST | `/process` | Clean text and calculate statistics |
| POST | `/sentiment` | Predict text sentiment |


### 1. Health Check

**Request**

```http
GET /
```

**Example response**

```json
{
  "message": "Welcome to BanglaText API!",
  "status": "running"
}
```

### 2. Process Text

**Request**

```http
POST /process
```

**Example request body**

```json
{
  "text": "  আমি বাংলা শিখি।   তুমি কি শিখো? "
}
```

The endpoint normalizes Unicode, removes extra whitespace, and returns cleaned text with basic statistics.

### 3. Analyze Sentiment

**Request**

```http
POST /sentiment
```

**Example request body**

```json
{
  "text": "এই পণ্যটির মান খুব ভালো, আমি সন্তুষ্ট।"
}
```

**Example response**

```json
{
  "text": "এই পণ্যটির মান খুব ভালো, আমি সন্তুষ্ট।",
  "sentiment": "positive",
  "model_score": 0.6258,
  "note": "AI prediction; results may be incorrect."
}
```

The sentiment model predicts one of three classes:

- `positive`
- `negative`
- `neutral`

The model score represents the model's confidence-like output for the predicted class. It is not a guarantee of correctness or a measure of real-world accuracy.

## 🧪 Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

The tests cover API availability, text processing, sentence counting, sentiment prediction, and input validation.

## 🤖 AI Model

The project uses the pretrained model [`gradienninja/bangla-sentiment-analyzer`](https://huggingface.co/gradienninja/bangla-sentiment-analyzer), based on BanglaBERT.

The model supports three sentiment classes. Its predictions may be incorrect, particularly for ambiguous, sarcastic, mixed-language, or context-dependent text. Real-world performance should be evaluated on a representative, labeled Bengali dataset before production use.

## 🌐 Deploy to Render

This repository is pre-configured for seamless deployment to [Render](https://render.com) as a Web Service.

### Option 1: Blueprint Deployment (Recommended)

1. Go to your [Render Dashboard](https://dashboard.render.com).
2. Click **New +** and select **Blueprint**.
3. Connect your GitHub repository: `https://github.com/nazrana-nahreen/banglatext-api`.
4. Render detects [`render.yaml`](render.yaml) automatically.
5. Click **Apply** to start building and deploying.

### Option 2: Manual Web Service Deployment

1. On Render, click **New +** -> **Web Service**.
2. Select your repository `banglatext-api`.
3. Set the following options:
   - **Name:** `banglatext-api`
   - **Runtime:** `Python`
   - **Branch:** `main`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path:** `/health`
4. Under **Advanced**, ensure the environment variable is set:
   - `PYTHON_VERSION`: `3.10.13`
5. Click **Create Web Service**.

> [!TIP]
> **Resource Recommendations:**
> - Endpoints `/` and `/process` (Unicode cleaning, tokenization, sentence statistics) run with low memory (< 60MB RAM).
> - The sentiment model (`gradienninja/bangla-sentiment-analyzer`) uses ~800MB peak RAM during inference. For sentiment analysis in production, Render's **Starter** (512MB–1GB) or **Standard** plan (2GB RAM) is recommended to prevent memory throttling.

## 🔒 Current Limitations

- No authentication or API key management yet.
- No rate limiting or usage tracking yet.
- Sentiment quality has not been independently evaluated on a representative test dataset.
- The pretrained model requires sufficient memory for AI inference.

## 🗺️ Roadmap

- [x] Build a FastAPI application.
- [x] Implement Bengali text processing.
- [x] Add pretrained sentiment analysis.
- [x] Add automated tests.
- [x] Deploy configuration for Render Web Service.
- [ ] Improve sentiment evaluation with labeled test data.
- [ ] Add API authentication and rate limiting.
- [ ] Add continuous integration with GitHub Actions.
- [ ] Explore additional Bengali NLP features.


## 👩‍💻 Author

**Nazrana Nahreen**

GitHub: [@nazrana-nahreen](https://github.com/nazrana-nahreen)

## 📄 License

No license has been added yet. Unless a license is added, others generally do not receive explicit permission to reuse, modify, or redistribute this code.
