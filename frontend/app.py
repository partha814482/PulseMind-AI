import streamlit as st
import requests

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="PulseMind AI",
    layout="centered"
)

st.title("🧠 PulseMind AI – Emotion-Aware Assistant")
st.caption("Analyze emotions from text or voice input")

BACKEND_URL = "http://127.0.0.1:8000"

# ------------------ TEXT INPUT ------------------
st.subheader("✍️ Text Emotion Analysis")

text = st.text_area(
    "Enter how you are feeling:",
    height=120,
    placeholder="Example: I am feeling very stressed and tired today"
)

if st.button("Analyze Text Emotion"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing text emotion..."):
            response = requests.post(
                f"{BACKEND_URL}/analyze_text",
                json={"text": text}
            )

        if response.status_code == 200:
            data = response.json()

            st.success("✅ Analysis Complete")

            st.subheader("Emotion Analysis")
            st.json(data["emotion_analysis"])

            st.subheader("AI Decision")
            st.info(data["ai_decision"]["message"])
        else:
            st.error("❌ Backend not responding")

# ------------------ VOICE INPUT ------------------
st.divider()
st.subheader("🎙️ Voice Emotion Analysis")

st.write(
    "Click the button below and speak clearly into your **earphone microphone**."
)

if st.button("🎙️ Analyze Voice Emotion"):
    with st.spinner("Listening... Please speak now"):
        response = requests.post(f"{BACKEND_URL}/analyze_voice")

    if response.status_code == 200:
        data = response.json()

        st.success("✅ Voice Analysis Complete")

        st.subheader("Recognized Speech")
        st.write(data["recognized_text"])

        st.subheader("Emotion Analysis")
        st.json(data["emotion_analysis"])

        st.subheader("AI Decision")
        st.info(data["ai_decision"]["message"])
    else:
        st.error("❌ Voice analysis failed")
