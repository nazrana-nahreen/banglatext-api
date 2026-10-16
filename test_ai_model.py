
from transformers import pipeline, AutoConfig

MODEL_NAME = "gradienninja/bangla-sentiment-analyzer"

# Model-এর label configuration দেখব
config = AutoConfig.from_pretrained(MODEL_NAME)
print("Model label mapping:", config.id2label)

# CPU-তে model চালাব
classifier = pipeline(
    "text-classification",
    model=MODEL_NAME,
    device=-1,
)

texts = [
    "এই পণ্যটির মান খুব ভালো, আমি সন্তুষ্ট।",
    "এই পণ্যটি খুব খারাপ, আমি একদমই সন্তুষ্ট নই।",
    "পণ্যটি আজ হাতে পেলাম।",
]

for text in texts:
    result = classifier(text)
    print("\nText:", text)
    print("Prediction:", result)
