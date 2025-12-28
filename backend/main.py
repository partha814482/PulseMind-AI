from fastapi import FastAPI
from models.text_emotion import TextEmotionAnalyzer
from models.voice_input import VoiceInput
from agent.decision_engine import DecisionEngine

app = FastAPI(
    title="PulseMind AI",
    description="Emotion-Aware Productivity AI (Text + Voice)",
    version="1.2.0"
)

emotion_model = TextEmotionAnalyzer()
decision_engine = DecisionEngine()
voice_input = VoiceInput()

@app.get("/")
def root():
    return {"status": "PulseMind AI Backend Running"}

@app.post("/analyze_text")
def analyze_text(data: dict):
    text = data.get("text", "")
    emotion_result = emotion_model.predict(text)

    decision = decision_engine.decide(
        emotion_result["emotion"],
        emotion_result["confidence"]
    )

    return {
        "input_type": "text",
        "emotion_analysis": emotion_result,
        "ai_decision": decision
    }

@app.post("/analyze_voice")
def analyze_voice():
    text = voice_input.listen()

    if text == "":
        return {"error": "Could not recognize speech"}

    emotion_result = emotion_model.predict(text)
    decision = decision_engine.decide(
        emotion_result["emotion"],
        emotion_result["confidence"]
    )

    return {
        "input_type": "voice",
        "recognized_text": text,
        "emotion_analysis": emotion_result,
        "ai_decision": decision
    }
