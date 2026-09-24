"""
AgriAI — Smart Crop Advisor (Basic Version)
College mini-project: crop recommendation, disease upload UI,
simple agricultural assistant, English + Tamil labels.

Run with:  streamlit run app.py
"""

import streamlit as st
from crop_model.predict import predict_crop, model_exists

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AgriAI — Smart Crop Advisor",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Simple English / Tamil labels ────────────────────────────────────────────
T = {
    "en": {
        "app_name": "AgriAI",
        "subtitle": "Smart Crop Advisor",
        "nav": "Navigate",
        "home": "Home",
        "crop": "Crop Recommendation",
        "disease": "Disease Detection",
        "assistant": "Agricultural Assistant",
        "about": "About",
        "lang": "Language",
        "home_intro": (
            "A simple AI-powered agriculture assistant built as a college mini-project. "
            "Get crop recommendations from soil and climate values, upload leaf images "
            "for disease detection (when a model is available), and ask basic farming questions."
        ),
        "home_features": "What can AgriAI do?",
        "feat_crop": "Recommend the best crop using soil nutrients and weather.",
        "feat_disease": "Upload a plant leaf image for disease detection.",
        "feat_assistant": "Ask simple agriculture questions and get clear answers.",
        "sidebar_hint": "Use the sidebar to open a feature.",
        "crop_title": "Crop Recommendation",
        "crop_help": "Enter soil and climate values. The Random Forest model predicts a suitable crop.",
        "n_label": "Nitrogen (N)",
        "p_label": "Phosphorus (P)",
        "k_label": "Potassium (K)",
        "temp_label": "Temperature (°C)",
        "hum_label": "Humidity (%)",
        "ph_label": "pH",
        "rain_label": "Rainfall (mm)",
        "predict_btn": "Recommend Crop",
        "result": "Recommended crop",
        "model_missing": "Crop model not found. Run: python crop_model/train.py",
        "disease_title": "Plant Disease Detection",
        "disease_help": "Upload a clear photo of a plant leaf.",
        "upload": "Upload leaf image",
        "disease_unavailable": "Disease detection model is not available yet.",
        "assistant_title": "Agricultural Assistant",
        "assistant_help": "Ask a basic farming question. Answers use built-in information (no paid API).",
        "ask_label": "Your question",
        "ask_btn": "Get Answer",
        "examples": "Example questions",
        "about_title": "About AgriAI",
        "about_body": (
            "**AgriAI — Smart Crop Advisor** is a basic college mini-project.\n\n"
            "### Technology\n"
            "- UI: Streamlit\n"
            "- Crop ML: Scikit-learn (Random Forest)\n"
            "- Disease: Upload interface only (model not trained yet)\n"
            "- Assistant: Predefined agricultural answers (no paid API)\n\n"
            "### Disclaimer\n"
            "For **educational purposes only**. Not a substitute for professional advice."
        ),
        "no_answer": "Sorry, I do not have information for that yet. Try one of the example questions.",
    },
    "ta": {
        "app_name": "AgriAI",
        "subtitle": "ஸ்மார்ட் பயிர் ஆலோசகர்",
        "nav": "வழிசெலுத்தல்",
        "home": "முகப்பு",
        "crop": "பயிர் பரிந்துரை",
        "disease": "நோய் கண்டறிதல்",
        "assistant": "விவசாய உதவியாளர்",
        "about": "பற்றி",
        "lang": "மொழி",
        "home_intro": (
            "கல்லூரி மினி-த் திட்டமாக உருவாக்கப்பட்ட எளிய விவசாய உதவி செயலி. "
            "மண் மற்றும் காலநிலை மதிப்புகளிலிருந்து பயிர் பரிந்துரை, "
            "இலை படம் பதிவேற்றம், மற்றும் அடிப்படை விவசாய கேள்விகள்."
        ),
        "home_features": "AgriAI என்ன செய்யும்?",
        "feat_crop": "மண் ஊட்டச்சத்து மற்றும் வானிலையைக் கொண்டு சிறந்த பயிரை பரிந்துரைக்கும்.",
        "feat_disease": "தாவர இலைப் படத்தை பதிவேற்றி நோய் கண்டறிய உதவும்.",
        "feat_assistant": "எளிய விவசாய கேள்விகளுக்கு பதிலளிக்கும்.",
        "sidebar_hint": "அம்சத்தைத் திறக்க பக்கப்பட்டி பயன்படுத்தவும்.",
        "crop_title": "பயிர் பரிந்துரை",
        "crop_help": "மண் மற்றும் காலநிலை மதிப்புகளை உள்ளிடவும். Random Forest மாதிரி பயிரை கணிக்கும்.",
        "n_label": "நைட்ரஜன் (N)",
        "p_label": "பாஸ்பரஸ் (P)",
        "k_label": "பொட்டாசியம் (K)",
        "temp_label": "வெப்பநிலை (°C)",
        "hum_label": "ஈரப்பதம் (%)",
        "ph_label": "pH",
        "rain_label": "மழைப்பொழிவு (mm)",
        "predict_btn": "பயிர் பரிந்துரை",
        "result": "பரிந்துரைக்கப்பட்ட பயிர்",
        "model_missing": "பயிர் மாதிரி இல்லை. இயக்கவும்: python crop_model/train.py",
        "disease_title": "தாவர நோய் கண்டறிதல்",
        "disease_help": "தாவர இலையின் தெளிவான படத்தை பதிவேற்றவும்.",
        "upload": "இலைப் படம் பதிவேற்றவும்",
        "disease_unavailable": "Disease detection model is not available yet.",
        "assistant_title": "விவசாய உதவியாளர்",
        "assistant_help": "அடிப்படை விவசாய கேள்வியைக் கேளுங்கள். உள்ளமைக்கப்பட்ட தகவல் பயன்படுத்தப்படும்.",
        "ask_label": "உங்கள் கேள்வி",
        "ask_btn": "பதில் பெறு",
        "examples": "எடுத்துக்காட்டு கேள்விகள்",
        "about_title": "AgriAI பற்றி",
        "about_body": (
            "**AgriAI — Smart Crop Advisor** என்பது அடிப்படை கல்லூரி மினி-த் திட்டம்.\n\n"
            "### தொழில்நுட்பம்\n"
            "- UI: Streamlit\n"
            "- பயிர் ML: Scikit-learn (Random Forest)\n"
            "- நோய்: பதிவேற்ற இடைமுகம் மட்டும் (மாதிரி இன்னும் இல்லை)\n"
            "- உதவியாளர்: முன்வரையறுக்கப்பட்ட பதில்கள் (கட்டண API இல்லை)\n\n"
            "### குறிப்பு\n"
            "**கல்வி நோக்கங்களுக்கு மட்டும்**. தொழில்முறை ஆலோசனைக்கு மாற்றாகாது."
        ),
        "no_answer": "இந்த கேள்விக்கு தகவல் இல்லை. எடுத்துக்காட்டு கேள்விகளை முயற்சிக்கவும்.",
    },
}

# Predefined assistant answers (English + Tamil)
ASSISTANT_KB = [
    {
        "keys": ["npk", "n p k", "nitrogen", "phosphorus", "potassium", "நைட்ரஜன்", "என்பிகே"],
        "en": (
            "**NPK** means **Nitrogen (N), Phosphorus (P), and Potassium (K)** — "
            "the three main nutrients plants need.\n\n"
            "- **N**: leaf growth and green color\n"
            "- **P**: roots, flowers, and fruits\n"
            "- **K**: overall plant strength and disease resistance"
        ),
        "ta": (
            "**NPK** என்பது **நைட்ரஜன் (N), பாஸ்பரஸ் (P), பொட்டாசியம் (K)** — "
            "தாவரங்களுக்கு தேவையான முக்கிய ஊட்டச்சத்துக்கள்.\n\n"
            "- **N**: இலை வளர்ச்சி மற்றும் பச்சை நிறம்\n"
            "- **P**: வேர், பூ, பழம்\n"
            "- **K**: தாவர வலிமை மற்றும் நோய் எதிர்ப்பு"
        ),
    },
    {
        "keys": ["high rainfall", "more rain", "needs rain", "அதிக மழை", "மழைப்பொழிவு"],
        "en": (
            "Crops that often need **high rainfall** include **rice**, and sometimes "
            "crops like **jute** or **coconut** depending on the region.\n\n"
            "In this project's crop dataset, **rice** is strongly linked with higher rainfall values. "
            "Always check local climate and irrigation before planting."
        ),
        "ta": (
            "**அதிக மழை** தேவைப்படும் பயிர்களில் **நெல் (rice)** முக்கியமானது. "
            "பிராந்தியத்தைப் பொறுத்து சணல் அல்லது தென்னை போன்றவை இருக்கலாம்.\n\n"
            "இந்த திட்டத்தின் தரவுத்தொகுப்பில் **நெல்** அதிக மழைப்பொழிவுடன் தொடர்புடையது. "
            "நடவுக்கு முன் உள்ளூர் காலநிலையைப் பார்க்கவும்."
        ),
    },
    {
        "keys": ["crop rotation", "rotation", "பயிர் சுழற்சி", "சுழற்சி"],
        "en": (
            "**Crop rotation** means growing different crops in the same field across seasons "
            "instead of the same crop every time.\n\n"
            "Benefits:\n"
            "- Improves soil health\n"
            "- Reduces pests and diseases\n"
            "- Helps balance nutrients (e.g., legumes add nitrogen)"
        ),
        "ta": (
            "**பயிர் சுழற்சி** என்பது ஒரே வயலில் ஒவ்வொரு பருவத்திலும் வெவ்வேறு பயிர்களை வளர்ப்பது.\n\n"
            "நன்மைகள்:\n"
            "- மண் ஆரோக்கியம் மேம்படும்\n"
            "- பூச்சி மற்றும் நோய் குறையும்\n"
            "- ஊட்டச்சத்து சமநிலை (எ.கா. பருப்பு வகைகள் நைட்ரஜன் சேர்க்கும்)"
        ),
    },
    {
        "keys": ["disease prevention", "prevent disease", "plant disease", "நோய் தடுப்பு", "நோய்"],
        "en": (
            "**Basic plant disease prevention:**\n\n"
            "1. Use healthy seeds and clean tools\n"
            "2. Avoid overwatering; keep good drainage\n"
            "3. Give enough spacing for air flow\n"
            "4. Remove infected leaves early\n"
            "5. Practice crop rotation\n"
            "6. Do not fake diagnoses — consult an expert for serious cases"
        ),
        "ta": (
            "**அடிப்படை தாவர நோய் தடுப்பு:**\n\n"
            "1. ஆரோக்கியமான விதை மற்றும் சுத்தமான கருவிகள்\n"
            "2. அதிக நீர் தவிர்க்கவும்; நல்ல வடிகால்\n"
            "3. காற்று ஓட்டத்திற்கு இடைவெளி\n"
            "4. பாதிக்கப்பட்ட இலைகளை விரைவில் அகற்றவும்\n"
            "5. பயிர் சுழற்சி செய்யவும்\n"
            "6. கடுமையான பிரச்சினைக்கு நிபுணரை அணுகவும்"
        ),
    },
    {
        "keys": ["fertilizer", "manure", "உரம்"],
        "en": (
            "Use fertilizer based on soil need. Too much fertilizer can harm plants and soil. "
            "Organic manure improves soil structure. Soil testing helps choose the right amount of NPK."
        ),
        "ta": (
            "மண் தேவைக்கு ஏற்ப உரம் பயன்படுத்தவும். அதிக உரம் தாவரம் மற்றும் மண்ணை பாதிக்கலாம். "
            "இயற்கை எரு மண் அமைப்பை மேம்படுத்தும். மண் பரிசோதனை NPK அளவை தேர்வு செய்ய உதவும்."
        ),
    },
    {
        "keys": ["irrigation", "watering", "நீர்ப்பாசனம்", "நீர்"],
        "en": (
            "Water plants based on crop type and soil. Early morning watering is often better. "
            "Avoid waterlogging. Drip irrigation saves water for many crops."
        ),
        "ta": (
            "பயிர் மற்றும் மண்ணைப் பொறுத்து நீர் ஊற்றவும். காலை நேர நீர்ப்பாசனம் பெரும்பாலும் சிறந்தது. "
            "நீர் தேங்கலைத் தவிர்க்கவும். சொட்டு நீர்ப்பாசனம் பல பயிர்களுக்கு நீர் சேமிக்கும்."
        ),
    },
]


def get_assistant_answer(question, lang):
    """Match question keywords to predefined answers. No paid API."""
    q = question.lower().strip()
    if not q:
        return None
    for item in ASSISTANT_KB:
        for key in item["keys"]:
            if key in q:
                return item[lang]
    return None


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌾 AgriAI")
    lang_choice = st.selectbox(
        "Language / மொழி",
        options=["English", "தமிழ்"],
        index=0,
    )
    lang = "ta" if lang_choice == "தமிழ்" else "en"
    t = T[lang]

    st.markdown("---")
    page = st.radio(
        t["nav"],
        [
            t["home"],
            t["crop"],
            t["disease"],
            t["assistant"],
            t["about"],
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("AgriAI — Basic Version")

# ── HOME ─────────────────────────────────────────────────────────────────────
if page == t["home"]:
    st.markdown(f"# 🌾 {t['app_name']}")
    st.markdown(f"### {t['subtitle']}")
    st.write(t["home_intro"])
    st.markdown("---")
    st.markdown(f"#### {t['home_features']}")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"**🌱 {t['crop']}**")
        st.write(t["feat_crop"])
    with c2:
        st.markdown(f"**📷 {t['disease']}**")
        st.write(t["feat_disease"])
    with c3:
        st.markdown(f"**🤖 {t['assistant']}**")
        st.write(t["feat_assistant"])

    st.info(t["sidebar_hint"])

# ── CROP RECOMMENDATION ──────────────────────────────────────────────────────
elif page == t["crop"]:
    st.markdown(f"# 🌱 {t['crop_title']}")
    st.write(t["crop_help"])

    if not model_exists():
        st.error(t["model_missing"])
    else:
        col1, col2 = st.columns(2)
        with col1:
            N = st.number_input(t["n_label"], min_value=0, max_value=140, value=90)
            P = st.number_input(t["p_label"], min_value=5, max_value=145, value=42)
            K = st.number_input(t["k_label"], min_value=5, max_value=205, value=43)
            temperature = st.number_input(
                t["temp_label"], min_value=0.0, max_value=50.0, value=20.9, step=0.1
            )
        with col2:
            humidity = st.number_input(
                t["hum_label"], min_value=0.0, max_value=100.0, value=82.0, step=0.1
            )
            ph = st.number_input(
                t["ph_label"], min_value=0.0, max_value=14.0, value=6.5, step=0.1
            )
            rainfall = st.number_input(
                t["rain_label"], min_value=0.0, max_value=300.0, value=202.9, step=0.1
            )

        if st.button(t["predict_btn"], type="primary"):
            crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
            st.success(f"**{t['result']}:** {crop}")

# ── DISEASE DETECTION ────────────────────────────────────────────────────────
elif page == t["disease"]:
    st.markdown(f"# 📷 {t['disease_title']}")
    st.write(t["disease_help"])

    uploaded = st.file_uploader(
        t["upload"],
        type=["jpg", "jpeg", "png"],
    )
    if uploaded is not None:
        st.image(uploaded, caption=uploaded.name, width=350)

    # No disease model in this basic version — do not fake predictions
    st.warning(t["disease_unavailable"])

# ── AGRICULTURAL ASSISTANT ───────────────────────────────────────────────────
elif page == t["assistant"]:
    st.markdown(f"# 🤖 {t['assistant_title']}")
    st.write(t["assistant_help"])

    st.markdown(f"**{t['examples']}:**")
    st.markdown(
        "- What is NPK?\n"
        "- Which crop needs high rainfall?\n"
        "- What is crop rotation?\n"
        "- Basic plant disease prevention"
    )

    question = st.text_input(t["ask_label"], placeholder="What is NPK?")
    if st.button(t["ask_btn"], type="primary"):
        answer = get_assistant_answer(question, lang)
        if answer:
            st.markdown(answer)
        else:
            st.info(t["no_answer"])

# ── ABOUT ────────────────────────────────────────────────────────────────────
elif page == t["about"]:
    st.markdown(f"# ℹ️ {t['about_title']}")
    st.markdown(t["about_body"])
