# 🌾 AgriAI – AI-Powered Smart Crop Advisor

AgriAI is an AI-powered agricultural assistant designed to help farmers and agriculture students get simple, practical, and personalized guidance about crops, soil, fertilizers, diseases, irrigation, and farming practices.

The application combines **Artificial Intelligence, Machine Learning, Natural Language Processing, and Voice Assistance** to provide an easy-to-use agricultural support system.

> 🌱 Making agricultural knowledge easier to access with AI.

---
🌐 *Try Agri AI Online:*

👉 [Open Agri AI](https://agri-ai-nspfd26du2qqvbfck9gtm9.streamlit.app/)

## 🚀 Features

### 🌾 Crop Advisory
Get recommendations and guidance based on crop-related requirements such as:

- Crop selection
- Soil conditions
- Weather considerations
- Water requirements
- Fertilizer usage
- Basic farming practices

### 🦠 Plant Disease Assistance
Users can describe plant symptoms and receive AI-generated information about:

- Possible plant diseases
- Common symptoms
- Possible causes
- Prevention methods
- Basic treatment suggestions

> **Note:** AI-generated suggestions are for educational and informational purposes and should not replace advice from agricultural experts.

### 💧 Irrigation Guidance

AgriAI can provide guidance related to:

- Water requirements
- Irrigation frequency
- Crop growth stages
- Basic water-management practices

### 🧪 Soil & Fertilizer Guidance

The system can provide information about:

- Soil requirements
- Nutrient requirements
- Fertilizer usage
- Soil preparation
- Basic nutrient management

### 🎙️ Tamil Voice Assistant

AgriAI is designed with a **Tamil-friendly voice interaction system** to make the application easier to use for Tamil-speaking users.

Users can interact with the system using voice instead of depending completely on typing.

### 🤖 AI Agricultural Assistant

Users can ask agricultural questions in natural language and receive AI-generated responses.

Example questions:

```text
Which crop is suitable for this soil?

How often should I water tomato plants?

What are the common diseases affecting rice?

What fertilizer is commonly used for tomato cultivation?

How can I prevent fungal diseases in crops?



🏗️ System Architecture
                ┌──────────────────────┐
                │       User           │
                └──────────┬───────────┘
                           │
                 Text / Voice Input
                           │
                           ▼
                ┌──────────────────────┐
                │   AgriAI Interface   │
                │      (Streamlit)     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Query Processing   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │      AI Engine       │
                │                      │
                │ NLP / LLM / ML       │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Agricultural         │
                │ Knowledge / Logic    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     AI Response      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Text / Voice Output  │
                └──────────────────────┘
🛠️ Technology Stack
Frontend
Streamlit
HTML
CSS
Programming Language
Python
Artificial Intelligence
Large Language Models
Natural Language Processing
Machine Learning
Voice Assistance
Speech-to-Text
Text-to-Speech
Tamil language support
Local AI

The project can be configured to use local AI models so that AI processing can be performed locally without depending completely on paid cloud APIs.

Possible local AI setup:

Ollama
Local LLMs
Development Tools
Python
VS Code
Git
GitHub
📁 Project Structure
AgriAI/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
├── assets/
│   └── images/
│
├── models/
│   └── ...
│
├── data/
│   └── ...
│
├── utils/
│   ├── ai.py
│   ├── voice.py
│   └── agriculture.py
│
└── .streamlit/
    └── config.toml

The exact structure may vary depending on the version of the project.

⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/AgriAI.git

Move into the project directory:

cd AgriAI
2. Create a Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

Usually:

http://localhost:8501
🤖 Local AI Setup

AgriAI can be configured to work with a locally running AI model using Ollama.

First install Ollama on your system.

Then download a compatible model:

ollama pull llama3.2

Start Ollama:

ollama serve

The AgriAI application can then communicate with the local model.

Advantages of Local AI
No per-request API cost
Can work without cloud AI services
Better privacy
Suitable for experimentation
Useful for student projects

Model requirements depend on the selected LLM.

🎙️ Tamil Voice Assistant

The voice assistant is intended to make AgriAI easier to use for Tamil-speaking users.

Example:

User:
"தக்காளி பயிருக்கு எந்த உரம் பயன்படுத்தலாம்?"

AgriAI:
Provides agricultural guidance in a user-friendly response.

The exact speech-to-text and text-to-speech implementation may vary depending on the configured voice libraries.

🌱 Example Use Cases
Farmer

A farmer can ask:

Which crop should I grow in this soil?

AgriAI can provide general crop-selection guidance.

Student

Agriculture or engineering students can use AgriAI to:

Learn about crops
Understand plant diseases
Explore farming techniques
Experiment with AI applications
Agricultural Knowledge Assistant

The system can act as a conversational interface for accessing agricultural information.

🔐 Privacy & Security

AgriAI is designed with privacy and security in mind.

Important practices:

Do not commit API keys to GitHub.
Store secrets in environment variables or Streamlit secrets.
Add sensitive files to .gitignore.
Avoid storing personal user information unnecessarily.

Example .gitignore:

.env
.streamlit/secrets.toml

__pycache__/
*.pyc

venv/
.venv/

models/
*.pkl
*.bin
*.gguf
💰 Cost

AgriAI can be configured as a zero-cost development project by using local AI models and open-source tools.

Possible costs may occur if you choose to use:

Cloud AI APIs
Paid hosting
External agricultural APIs
Paid speech services

Using local models can significantly reduce recurring API costs.

🔮 Future Improvements

Planned and possible improvements include:

📱 Mobile-friendly interface
🌦️ Real-time weather integration
🗺️ Location-based crop recommendations
🌾 More crop-specific recommendations
🦠 Image-based plant disease detection
🎙️ Improved Tamil voice interaction
🗣️ Multi-language support
📊 Crop yield prediction
💧 Smart irrigation recommendations
🧪 Soil analysis
📈 Crop price information
👨‍🌾 Farmer-focused dashboard
📚 Agricultural knowledge base
🔍 RAG-based agricultural question answering
📷 Plant image analysis
🎯 Project Goals

The main goals of AgriAI are:

Make agricultural information easier to access.
Provide AI-assisted crop guidance.
Support Tamil-language interaction.
Explore the application of AI in agriculture.
Build an affordable and accessible agricultural assistant.
Demonstrate the practical use of AI/ML in a real-world problem.
🧠 AI/ML Concepts Demonstrated

This project provides practical exposure to:

Artificial Intelligence
Machine Learning
Natural Language Processing
Large Language Models
Speech Recognition
Text-to-Speech
Prompt Engineering
Local LLMs
API Integration
Streamlit Application Development
📸 Screenshots

Add screenshots of your application here.

Example:

screenshots/
├── home.png
├── crop-advisor.png
├── voice-assistant.png
└── result.png

You can then add them to this README:

![AgriAI Home](screenshots/home.png)
🚀 Future Vision

AgriAI aims to evolve from a simple AI agricultural assistant into a more complete AI-powered farming support platform.

The long-term vision includes:

AI Crop Advisor
       +
Plant Disease Detection
       +
Weather Intelligence
       +
Soil Analysis
       +
Tamil Voice Assistant
       +
Yield Prediction
       +
Smart Irrigation
       ↓
AI-Powered Agriculture Platform
👨‍💻 Developer

Navamani Kandan

B.Tech CSE (AI & ML) Student

Interested in:

Artificial Intelligence
Machine Learning
Software Development
Generative AI
Real-world AI Applications
⭐ Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

git clone https://github.com/YOUR_USERNAME/AgriAI.git

Create a new branch:

git checkout -b feature/new-feature

Make your changes and commit:

git add .
git commit -m "Add new feature"

Push the branch:

git push origin feature/new-feature

Then create a Pull Request.

📄 License

This project is intended for educational and research purposes.

You may add an appropriate open-source license such as MIT License depending on how you want to distribute the project.
