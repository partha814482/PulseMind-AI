from transformers import pipeline

class TextEmotionAnalyzer:
    def __init__(self):
        self.classifier = pipeline(
            task="text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            framework="pt",              # 🔥 FORCE PYTORCH
            return_all_scores=True
        )

    def predict(self, text: str):
        results = self.classifier(text)[0]
        top_emotion = max(results, key=lambda x: x["score"])

        return {
            "emotion": top_emotion["label"],
            "confidence": round(top_emotion["score"], 3)
        }
