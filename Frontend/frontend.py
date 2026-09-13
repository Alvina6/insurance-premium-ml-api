import streamlit as st
import requests


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🏥",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🏥 Insurance Premium Predictor")
st.write(
    "Enter the user's details to predict the insurance premium category."
)


# -----------------------------
# User Input
# -----------------------------

age = st.number_input(
    "Age",
    min_value=1,
    max_value=99,
    value=25
)

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    max_value=300.0,
    value=60.0
)

height = st.number_input(
    "Height (meters)",
    min_value=0.5,
    max_value=2.5,
    value=1.65
)

income_lpa = st.number_input(
    "Annual Income (LPA)",
    min_value=0.1,
    value=5.0
)

smoker = st.selectbox(
    "Are you a smoker?",
    ["No", "Yes"]
)

city = st.text_input(
    "City",
    value="Mumbai"
)


occupations = [
    "Factory Worker",
    "Businessman",
    "Sales Manager",
    "Banker",
    "Marketing Manager",
    "Insurance Agent",
    "HR Manager",
    "Pharmacist",
    "Teacher",
    "Software Engineer",
    "Consultant",
    "Driver",
    "Shop Owner",
    "Nurse",
    "Accountant",
    "Government Employee",
    "Architect",
    "Engineer",
    "Real Estate Agent",
    "Civil Servant",
    "Plumber",
    "Retail Manager",
    "Chef",
    "Electrician",
    "Carpenter",
    "Doctor",
    "Lab Technician",
    "Data Analyst",
    "Lawyer",
    "Content Writer"
]

occupation = st.selectbox(
    "Occupation",
    occupations
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Premium Category"):

    data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker == "Yes",
        "city": city,
        "occupation": occupation
    }

    try:

        response = requests.post(
            "http://backend:8000/predict",
            json=data
        )

        # -----------------------------
        # Successful Response
        # -----------------------------

        if response.status_code == 200:

            result = response.json()

            predicted_category = result["predicted_category"]
            confidence = result["confidence"]
            probabilities = result["class_probabilities"]

            st.success(
                f"Predicted Category: {predicted_category}"
            )

            st.metric(
                "Confidence",
                f"{confidence * 100:.1f}%"
            )

            st.subheader("Class Probabilities")

            for category, probability in probabilities.items():

                st.write(
                    f"**{category}** — {probability * 100:.1f}%"
                )

                st.progress(probability)


        # -----------------------------
        # Validation Error
        # -----------------------------

        elif response.status_code == 422:

            st.error(
                "Invalid input. Please check your values."
            )

            st.json(response.json())


        # -----------------------------
        # Other Backend Errors
        # -----------------------------

        else:

            st.error(
                f"Backend error: {response.status_code}"
            )

            try:
                st.json(response.json())

            except requests.exceptions.JSONDecodeError:
                st.code(response.text)


    # -----------------------------
    # FastAPI Connection Error
    # -----------------------------

    except requests.exceptions.ConnectionError:

        st.error(
            "Cannot connect to FastAPI. "
            "Make sure your FastAPI server is running."
        )
