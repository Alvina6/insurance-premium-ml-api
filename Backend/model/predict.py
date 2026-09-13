import pickle
import pandas as pd

# Load trained model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

# SAFE FIX FOR LINE 10: Pipeline ke aakhri step se trained classes nikalna
if hasattr(model, "classes_"):
    class_labels = model.classes_.tolist()
elif hasattr(model, "steps"):
    # Agar model pipeline hai, to aakhri step (classifier) ko check karo
    final_estimator = model.steps[-1][1]  # Steps tuple format me hote hain: ('name', object)
    if hasattr(final_estimator, "classes_"):
        class_labels = final_estimator.classes_.tolist()
    else:
        class_labels = []
else:
    class_labels = []

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])

    # 1. Model Prediction
    raw_output = model.predict(input_df)
    predicted_category = raw_output.item() if hasattr(raw_output, "item") else raw_output

    # 2. Probabilities & Confidence
    probabilities = model.predict_proba(input_df)[0]  # First row ki probabilities
    raw_confidence = max(probabilities)
    confidence = raw_confidence.item() if hasattr(raw_confidence, "item") else raw_confidence

    # 3. Class Probabilities Dictionary Mapping
    class_probs = {}
    if class_labels:
        class_probs = {
            str(label): round(prob.item() if hasattr(prob, "item") else prob, 4)
            for label, prob in zip(class_labels, probabilities)
        }
    else:
        # Agar labels kisi wajah se nahi mile, to fallback to default index
        class_probs = {
            f"class_{i}": round(prob.item() if hasattr(prob, "item") else prob, 4)
            for i, prob in enumerate(probabilities)
        }

    return {
        "predicted_category": predicted_category,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
