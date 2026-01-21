import os
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
LOCAL_MODEL_PATH = "models"

def load_model():
    model_path = os.path.join(LOCAL_MODEL_PATH, MODEL_NAME)
    print(model_path)
    if not os.path.exists(model_path):
        print(f"[INFO] Model {MODEL_NAME} not found locally. Downloading ...")
        SentenceTransformer(MODEL_NAME)
    return SentenceTransformer(model_path)
