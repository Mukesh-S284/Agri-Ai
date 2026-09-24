"""
crop_model/predict.py
=====================
Load the trained Random Forest model and predict a crop.

Usage from app:
    from crop_model.predict import predict_crop
    crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
"""

import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

_model = None


def load_model():
    """Load and cache the trained model from disk."""
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model not found at {MODEL_PATH}. "
                "Run: python crop_model/train.py"
            )
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    """
    Predict the best crop for the given soil and climate values.

    Returns:
        str: predicted crop name
    """
    model = load_model()
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(features)
    return str(prediction[0])


def model_exists():
    """Return True if model.pkl is present."""
    return os.path.exists(MODEL_PATH)
