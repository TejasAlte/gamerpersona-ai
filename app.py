import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# ===============================
# Load Model (Cached)
# ===============================

@st.cache_resource
def load_model():
    model = joblib.load("models/model.pkl")
    encoders = joblib.load("models/encoders.pkl")
    return model, encoders

model, encoders = load_model()


# ===============================
# Radar Chart
# ===============================

def plot_radar(intensity, sleep, emotion, social, discipline):

    categories = ['INTENSITY', 'SLEEP', 'EMOTION', 'SOCIAL', 'DISCIPLINE']
    values = [intensity, sleep, emotion, social, discipline]

    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))

    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    ax.spines['polar'].set_visible(False)
    ax.grid(False)

    for level in [20, 40, 60, 80, 100]:
        ax.plot(angles, [level]*len(angles),
                color='#1C2333',
                linewidth=0.8)

    ax.plot(angles, values,
            linewidth=2.5,
            color='#3EF0B5')

    ax.fill(angles, values,
            color='#3EF0B5',
            alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories,
                       fontsize=11,
                       fontweight='bold',
                       color='#D6E4F0')

    ax.set_yticklabels([])
    ax.set_ylim(0, 100)

    return fig


# ===============================
# Sidebar Inputs
# ===============================

with st.sidebar:

    st.header("🎮 Gamer Profile")

    age = st.number_input("Age", 10, 60, 20)
    # gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    gender = st.selectbox("Gender", encoders["gender"].classes_)
    # game_genre = st.selectbox("Game Genre", ["Mobile Games", "FPS", "RPG", "MOBA", "Battle Royale", "Sports", "Other"])
    game_genre = st.selectbox("Game Genre", encoders["game_genre"].classes_)
    # gaming_platform = st.selectbox("Gaming Platform", ["PC", "Console", "Mobile"])
    gaming_platform= st.selectbox("Gaming Platform", encoders["gaming_platform"].classes_)
    daily_hours = st.slider("Daily Gaming Hours", 0.0, 16.0, 4.0)
    years_gaming = st.slider("Years Gaming", 0, 20, 3)
    monthly_spending = st.slider("Monthly Game Spending (USD)", 0.0, 500.0, 50.0)
    st.subheader("Sleep")
    sleep_hours = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
    # sleep_quality = st.selectbox("Sleep Quality", ["Very Poor", "Poor", "Average", "Good", "Very Good"])
    sleep_quality = st.selectbox("Sleep Quality", encoders["sleep_quality"].classes_)
    # sleep_disruption_frequency = st.selectbox("Sleep Disruption Frequency", ["Never", "Rarely", "Sometimes", "Often"])
    sleep_disruption_frequency = st.selectbox("Sleep Disruption Frequency", encoders["sleep_disruption_frequency"].classes_)

    st.subheader("Emotional")
    # mood_state = st.selectbox("Mood State", ["Neutral", "Happy", "Anxious", "Sad", "Irritable"])
    mood_state = st.selectbox(
    "Mood State",
    encoders["mood_state"].classes_)
    # mood_swing_frequency = st.selectbox("Mood Swing Frequency", ["Never", "Rarely", "Sometimes", "Often"])
    mood_swing_frequency = st.selectbox("Mood Swing Frequency", encoders["mood_swing_frequency"].classes_)
    withdrawal_symptoms = st.selectbox("Withdrawal Symptoms", [True, False])
    loss_of_other_interests = st.selectbox("Loss of Other Interests", [True, False])
    continued_despite_problems = st.selectbox("Continued Despite Problems", [True, False])

    st.subheader("Physical")
    eye_strain = st.selectbox("Eye Strain", [True, False])
    back_neck_pain = st.selectbox("Back / Neck Pain", [True, False])
    weight_change_kg = st.slider("Weight Change (kg)", -10.0, 10.0, 0.0)
    exercise_hours_weekly = st.slider("Exercise Hours Weekly", 0.0, 15.0, 3.0)

    st.subheader("Social")
    social_isolation_score = st.slider("Social Isolation Score", 1, 10, 3)
    face_to_face_social_hours_weekly = st.slider("Face-to-Face Social Hours Weekly", 0.0, 40.0, 10.0)

    st.subheader("Academic")
    # academic_work_performance = st.selectbox("Performance", ["Excellent", "Good", "Average", "Below Average", "Poor"])
    academic_work_performance = st.selectbox(
    "Performance",
    encoders["academic_work_performance"].classes_)
    grades_gpa = st.number_input("GPA (0–10)", 0.0, 10.0, 7.0)
    work_productivity_score = st.slider("Work Productivity Score", 0.0, 10.0, 7.0)


# ===============================
# Create Input Dict
# ===============================

user_input = {
    "age": age,
    "gender": gender,
    "daily_gaming_hours": daily_hours,
    "game_genre": game_genre,
    "gaming_platform": gaming_platform,
    "sleep_hours": sleep_hours,
    "sleep_quality": sleep_quality,
    "sleep_disruption_frequency": sleep_disruption_frequency,
    "academic_work_performance": academic_work_performance,
    "grades_gpa": grades_gpa,
    "work_productivity_score": work_productivity_score,
    "mood_state": mood_state,
    "mood_swing_frequency": mood_swing_frequency,
    "withdrawal_symptoms": withdrawal_symptoms,
    "loss_of_other_interests": loss_of_other_interests,
    "continued_despite_problems": continued_despite_problems,
    "eye_strain": eye_strain,
    "back_neck_pain": back_neck_pain,
    "weight_change_kg": weight_change_kg,
    "exercise_hours_weekly": exercise_hours_weekly,
    "social_isolation_score": social_isolation_score,
    "face_to_face_social_hours_weekly": face_to_face_social_hours_weekly,
    "monthly_game_spending_usd": monthly_spending,
    "years_gaming": years_gaming
}

input_df = pd.DataFrame([user_input])

# Ensure correct column order
model_features = model.feature_names_in_
input_df = input_df[model_features]

# Encode categorical
for col, encoder in encoders.items():
    if col in input_df.columns:
        input_df[col] = encoder.transform(input_df[col])

# ===============================
# Predict
# ===============================

prediction = model.predict(input_df)[0]
probabilities = model.predict_proba(input_df)[0]

risk_label = encoders["gaming_addiction_risk_level"].classes_[prediction]

# ===============================
# MAIN DISPLAY
# ===============================

st.title("🎮 GamerPersona AI")
st.subheader("ML-Powered Behavioral Insight")

st.markdown("---")

st.header("🎯 Addiction Risk Prediction")
st.subheader(f"Predicted Level: {risk_label}")

classes = encoders["gaming_addiction_risk_level"].classes_

prob_df = pd.DataFrame({
    "Risk Level": classes,
    "Probability": probabilities
})

st.write("### Risk Distribution")
st.bar_chart(prob_df.set_index("Risk Level"))

# ===============================
# Pentagon Stats
# ===============================

intensity = daily_hours * 6
sleep_score = 100 - abs(7 - sleep_hours) * 12
emotion_score = 70 if mood_state in ["Anxious", "Sad"] else 40
social_score = 100 - (social_isolation_score * 8)
discipline_score = exercise_hours_weekly * 10

st.write("### 🌌 Behavioral Energy Map")
radar = plot_radar(intensity, sleep_score, emotion_score, social_score, discipline_score)
st.pyplot(radar)
