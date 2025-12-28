class DecisionEngine:
    def decide(self, emotion: str, confidence: float):
        if confidence > 0.75:
            if emotion in ["anger", "frustration"]:
                return {
                    "action": "suggest_break",
                    "message": "You seem stressed. Take a short break and revisit the task calmly."
                }
            elif emotion in ["sadness"]:
                return {
                    "action": "encourage",
                    "message": "It’s okay to feel low. Try breaking your work into small steps."
                }

        return {
            "action": "normal",
            "message": "You seem fine. Continue working productively."
        }
