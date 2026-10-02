# AgriAI — Smart Crop Advisor (Basic Version)

A simple Streamlit agriculture mini-project for crop recommendation, disease upload UI, and a basic farming assistant.

## Features

- **Crop Recommendation** — Random Forest (scikit-learn)
- **Disease Detection** — image upload UI (model not available yet)
- **Agricultural Assistant** — predefined answers (no paid API)
- **English + Tamil** — UI language selector

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train the crop recommendation model (once)
python crop_model/train.py

# 3. Launch the app
streamlit run app.py
```

## Project Structure

```
AgriAi/
├── app.py                  ← Main Streamlit application
├── requirements.txt
├── README.md
├── crop_model/
│   ├── train.py            ← Train Random Forest model
│   ├── predict.py          ← Prediction helper
│   └── model.pkl           ← Saved model (after training)
└── data/
    └── crop_data.csv       ← Crop recommendation dataset
```

## Tech Stack

| Component   | Technology                    |
|-------------|-------------------------------|
| UI          | Streamlit                     |
| Crop ML     | Scikit-learn (Random Forest)  |
| Disease     | Upload UI only (no model yet) |
| Assistant   | Predefined text answers       |
| Language    | Python 3                      |

> **Disclaimer**: Educational purposes only. Not a substitute for professional advice.
