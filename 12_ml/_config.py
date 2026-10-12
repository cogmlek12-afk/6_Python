"""
    공통 항목 설정
"""
import os

BASE_DIR = os.path.dirname( os.path.abspath(__file__))
# ~/12_ml
DATA_DIR = os.path.join(BASE_DIR, "data")
# ~/12_ml/data
MODEL_DIR = os.path.join(BASE_DIR, "models")
# ~/12_ml/models

BASE_URL = "https://kh-lab.rockua.ai.kr/"

ENCODING = "utf-8-sig"

def path(name):
    return os.path.join(DATA_DIR, name)

def prices_path():
    local = path("prices.csv")

    if os.path.exists(local):
        return local

    return f"{BASE_URL}/datasets.prices.csv"

def model_path(name="model_bundle.pkl"):

    os.makedirs(MODEL_DIR, exist_ok=True)
    return os.path.join(MODEL_DIR, name)