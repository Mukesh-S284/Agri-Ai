"""
crop_model/train.py
====================
Train a Random Forest Classifier on the Crop Recommendation dataset.

Usage:
    python crop_model/train.py

Outputs:
    crop_model/model.pkl   -- trained Random Forest model
    crop_model/label_classes.pkl -- ordered class list (for reference)
"""

import os
import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)
import joblib

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
DATA_PATH  = os.path.join(BASE_DIR, "..", "data", "crop_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
LABEL_PATH = os.path.join(BASE_DIR, "label_classes.pkl")

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
TARGET   = "label"


def train():
    # ── 1. Load dataset ───────────────────────────────────────────────────────
    print("=" * 60)
    print("  AgriAI — Crop Recommendation Model Training")
    print("=" * 60)

    if not os.path.exists(DATA_PATH):
        print(f"\n[ERROR] Dataset not found at: {DATA_PATH}")
        print("Please place crop_data.csv in the data/ folder and retry.")
        sys.exit(1)

    print(f"\n[1] Loading dataset from: {os.path.abspath(DATA_PATH)}")
    df = pd.read_csv(DATA_PATH)

    # ── 2. Check dataset shape ────────────────────────────────────────────────
    print(f"\n[2] Dataset Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"    Columns: {list(df.columns)}")

    # ── 3. Check missing values ───────────────────────────────────────────────
    print(f"\n[3] Missing Values:")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("    None — dataset is complete.")
    else:
        print(missing[missing > 0])

    # ── 4. Unique crop labels ─────────────────────────────────────────────────
    labels = sorted(df[TARGET].unique())
    print(f"\n[4] Unique Crops ({len(labels)}): {labels}")

    # ── 5. Feature / target split ─────────────────────────────────────────────
    X = df[FEATURES].values
    y = df[TARGET].values
    print(f"\n[5] Features : {FEATURES}")
    print(f"    Target   : '{TARGET}'")

    # ── 6. Train / test split ─────────────────────────────────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"\n[6] Train/Test Split (80/20, stratified):")
    print(f"    Training samples : {len(X_train)}")
    print(f"    Testing  samples : {len(X_test)}")

    # ── 7. Train Random Forest ────────────────────────────────────────────────
    print("\n[7] Training RandomForestClassifier (n_estimators=100) ...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    print("    Training complete.")

    # ── 8. Evaluate on test set ───────────────────────────────────────────────
    y_pred = model.predict(X_test)

    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="weighted", zero_division=0)
    rec  = recall_score(y_test, y_pred, average="weighted", zero_division=0)
    f1   = f1_score(y_test, y_pred, average="weighted", zero_division=0)

    print("\n" + "=" * 60)
    print("  Model Evaluation — Actual Test Set Results")
    print("=" * 60)
    print(f"  Accuracy  : {acc * 100:.2f}%")
    print(f"  Precision : {prec:.4f}  (weighted)")
    print(f"  Recall    : {rec:.4f}  (weighted)")
    print(f"  F1-Score  : {f1:.4f}  (weighted)")
    print("=" * 60)

    print("\nPer-class Classification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # Confusion matrix (compact — just dimensions)
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    print(f"Confusion Matrix: {cm.shape[0]}x{cm.shape[1]} matrix computed.")
    print(f"  Diagonal sum (correct): {cm.diagonal().sum()} / {len(y_test)}")

    # ── 9. Save model ─────────────────────────────────────────────────────────
    joblib.dump(model, MODEL_PATH)
    joblib.dump(labels, LABEL_PATH)

    print(f"\n[9] Model saved  : {MODEL_PATH}")
    print(f"    Labels saved : {LABEL_PATH}")
    print("\nTraining complete. You can now run the Streamlit app.")
    return acc


if __name__ == "__main__":
    train()
