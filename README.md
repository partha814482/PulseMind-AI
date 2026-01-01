

# 🌟 PulseMind AI
### Emotion-Aware Agentic AI with Text & Voice Input

PulseMind AI is a **multimodal, emotion-aware agentic AI system** that analyzes **human emotions from text and voice inputs** and generates **intelligent, context-aware decisions** to support productivity, stress management, and mental well-being.

This project demonstrates a **real-world end-to-end AI application**, combining NLP, speech recognition, agent-based reasoning, REST APIs, and an interactive frontend.

---

## 📌 Project Overview

PulseMind AI allows users to:
- Enter **text** describing their feelings  
- Or use **voice input (earphone microphone)**  
- Detect emotions using a **pretrained NLP model**
- Apply an **agentic decision engine**
- Receive actionable AI-generated suggestions

---

## 🧠 Working Architecture

```

User (Text / Voice)
↓
Streamlit Frontend (UI)
↓
FastAPI Backend (API Layer)
↓
Emotion Detection Model (NLP)
↓
Agentic Decision Engine
↓
AI Recommendation / Action

```

### 🔹 Text Flow
```

Text Input
→ NLP Emotion Model
→ Emotion + Confidence
→ Agentic Decision

```

### 🔹 Voice Flow
```

Voice Input (Mic)
→ Speech-to-Text
→ NLP Emotion Model
→ Agentic Decision

```

---

## 🧩 Folder Architecture

```

PulseMind-AI/
│
├── backend/
│   └── main.py                # FastAPI backend (text + voice endpoints)
│
├── frontend/
│   └── app.py                 # Streamlit UI
│
├── models/
│   ├── text_emotion.py        # Text emotion detection model
│   └── voice_input.py         # Voice input (speech recognition)
│
├── agent/
│   └── decision_engine.py     # Agentic AI logic
│
├── utils/                     # Helper utilities (future use)
│
├── requirements.txt           # Required libraries
├── .gitignore
└── README.md

```

---

## ⚙️ Libraries & Tools Used

### 🔹 Backend
- **FastAPI** – REST API framework
- **Uvicorn** – ASGI server

### 🔹 AI / ML
- **Transformers (HuggingFace)** – NLP model inference
- **PyTorch** – Deep learning backend
- **SpeechRecognition** – Voice-to-text conversion
- **PyAudio** – Microphone audio capture

### 🔹 Frontend
- **Streamlit** – Interactive UI
- **Requests** – API communication

### 🔹 Other
- Python 3.10+
- Git & GitHub

---

## 🤖 AI Model Used

### 🧠 Text Emotion Detection Model

**Model Name:**
```

j-hartmann/emotion-english-distilroberta-base

````

**Why this model?**
- Pretrained on emotion-labeled English text
- Lightweight and fast
- High accuracy for emotion classification
- Suitable for real-time inference

**Detected Emotions Include:**
- Anger
- Sadness
- Fear
- Joy
- Neutral

---

## 🧠 Agentic Decision Engine

The agentic layer analyzes:
- Detected emotion
- Confidence score

Based on rules, it decides:
- Suggest a break
- Encourage user
- Normal continuation

Example:
```json
{
  "action": "suggest_break",
  "message": "You seem stressed. Take a short break and revisit the task calmly."
}
````

---

## 🖥️ Frontend Description (Streamlit)

The frontend provides:

* ✍️ Text input area
* 🎙️ Voice input button
* Emotion visualization
* AI decision display

It communicates with backend endpoints:

* `/analyze_text`
* `/analyze_voice`

---

## 🌐 Backend API Endpoints

### 🔹 Root

```
GET /
```

Returns backend health status.

---

### 🔹 Analyze Text Emotion

```
POST /analyze_text
```

**Input**

```json
{
  "text": "I am feeling very stressed and tired today"
}
```

---

### 🔹 Analyze Voice Emotion

```
POST /analyze_voice
```

* Uses system microphone
* Converts speech → text
* Analyzes emotion

---

## ▶️ How to Run the Project

### 1️⃣ Create & Activate Environment

```bash
conda create -n guduenv python=3.11 -y
conda activate guduenv
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Backend (Terminal 1)

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

---

### 4️⃣ Run Frontend (Terminal 2)

```bash
streamlit run frontend/app.py
```

Frontend URL:

```
http://localhost:8501
```
<img width="1917" height="877" alt="Screenshot 2026-01-01 201503" src="https://github.com/user-attachments/assets/b6d99394-cbdc-4047-807d-9115b4bd1ada" />
<img width="1919" height="887" alt="Screenshot 2026-01-01 201436" src="https://github.com/user-attachments/assets/f8330664-84c9-4907-a0a4-1b343a305886" />
<img width="1919" height="873" alt="Screenshot 2026-01-01 200945" src="https://github.com/user-attachments/assets/dfa50e66-05f6-43d0-9b0e-d17fe748d13a" />

---

## 🎯 Real-World Use Cases

* Mental health awareness tools
* Stress & burnout detection
* Emotion-aware productivity assistants
* Human-centric AI systems
* Affective computing research

---

## 🚀 Future Enhancements

* Voice response (Text-to-Speech)
* Emotion history tracking
* Burnout score visualization
* Cloud deployment (AWS / Azure)
* Mobile-friendly UI
* Advanced agent reasoning

---

## 👤 Author

**Parthasarathi Behera**
Aspiring AI Engineer | Data Science & Generative AI Enthusiast






