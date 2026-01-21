#!/bin/bash
set -e

echo "Installing Python dependencies..."
pip install -r requirement.txt

echo "Downloading SentenceTransformer model..."
python << 'EOF'
from sentence_transformers import SentenceTransformer
import os

MODEL_NAME = "all-MiniLM-L6-v2"
LOCAL_MODEL_PATH = "./models/all-MiniLM-L6-v2"

os.makedirs(LOCAL_MODEL_PATH, exist_ok=True)

print(f"Downloading model: {MODEL_NAME}")
model = SentenceTransformer(MODEL_NAME)
model.save(LOCAL_MODEL_PATH)

print(f"Model saved at: {LOCAL_MODEL_PATH}")
EOF

