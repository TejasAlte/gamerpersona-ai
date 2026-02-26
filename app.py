# ============================================
# GAMER BEHAVIOR ANALYSIS & RISK AI PLATFORM
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

# ============================================
# CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Gamer Behavior AI Analyzer",
    page_icon="🎮",
    layout="wide"
)

# ============================================
# MODEL LOADING
# ============================================

@st.cache_resource
def load_models():
    addiction_package = joblib.load("gaming_addiction_model.pkl")
    strain_package = joblib.load("gaming_physical_strain_model.pkl")

    return (
        addiction_package["model"],
        addiction_package["features"],
        strain_package["model"],
        strain_package["features"]
    )

addiction_model, addiction_features, strain_model, strain_features = load_models()

# ============================================
# SPIRIT ANIMAL DATABASE
# ============================================

spirit_animals = {
    "Wolf": {"traits": [0.80,0.75,0.70,0.90,0.75,0.60],
             "archetype":"Strategic Pack Leader",
             "description":"Driven, loyal, thrives in structured teamwork."},

    "Falcon": {"traits":[0.90,0.85,0.70,0.40,0.80,0.75],
               "archetype":"Precision Hunter",
               "description":"Focused and fast decision-maker."},

    "Cheetah":{"traits":[0.98,0.60,0.50,0.30,0.70,0.85],
               "archetype":"Burst Performer",
               "description":"Explosive energy with fast recovery."},

    "Elephant":{"traits":[0.60,0.85,0.95,0.90,0.55,0.80],
                "archetype":"Enduring Pillar",
                "description":"Stable and resilient."},

    "Phoenix":{"traits":[0.85,0.90,0.95,0.60,0.95,1.00],
               "archetype":"Rebirth Warrior",
               "description":"Rises stronger after setbacks."},

    "Owl":{"traits":[0.55,0.80,0.50,0.30,0.85,0.60],
           "archetype":"Nocturnal Strategist",
           "description":"Calm, analytical and thrives at night."}
}

# ============================================
# UTILITY FUNCTIONS
# ============================================

def build_feature_dataframe(user_dict, feature_order):
    df = pd.DataFrame([user_dict])
    df = df.reindex(columns=feature_order, fill_value=0)
    return df

def interpret_risk(label):
    mapping = {
        0: ("Low", "Low behavioral risk detected."),
        1: ("Moderate", "Moderate signs of behavioral dependency."),
        2: ("High", "High addiction risk. Lifestyle intervention recommended.")
    }
    return mapping.get(label, ("Unknown", "Unable to determine risk level."))

def build_user_traits(gaming, sleep, exercise, isolation, health_risk):
    intensity = min(gaming/10,1)
    discipline = min(sleep/8,1)
    endurance = min(exercise/7,1)
    sociality = 1 - min(isolation/10,1)
    adaptability = 1 - min(health_risk,1)
    recovery = min(sleep/9,1)

    return np.array([[intensity, discipline, endurance,
                      sociality, adaptability, recovery]])

def match_spirit_animal(user_vector):
    names = []
    vectors = []

    for name,data in spirit_animals.items():
        names.append(name)
        vectors.append(data["traits"])

    sims = cosine_similarity(user_vector, np.array(vectors))[0]
    top_idx = sims.argsort()[::-1][:3]

    results = []
    for idx in top_idx:
        results.append({
            "animal": names[idx],
            "score": round(float(sims[idx]),3),
            "archetype": spirit_animals[names[idx]]["archetype"],
            "description": spirit_animals[names[idx]]["description"]
        })
    return results

def plot_radar(traits):
    labels = ["Intensity","Discipline","Endurance",
              "Sociality","Adaptability","Recovery"]

    values = traits.flatten().tolist()
    values += values[:1]

    angles = np.linspace(0,2*np.pi,len(labels),endpoint=False).tolist()
    angles += angles[:1]

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0,1)

    return fig

# ============================================
# UI
# ============================================

st.title("🎮 Gamer Behavior Analysis & Addiction Risk AI")
st.markdown("AI-powered behavioral and health risk assessment system.")

with st.sidebar:
    st.header("User Input")

    gaming_hours = st.slider("Daily Gaming Hours", 0, 12, 4)
    spending = st.number_input("Monthly Game Spending ($)", 0, 1000, 50)
    sleep_hours = st.slider("Sleep Hours", 0, 12, 7)
    exercise_hours = st.slider("Exercise Hours Weekly", 0, 14, 3)
    social_isolation = st.slider("Social Isolation Score", 0, 10, 4)

    analyze = st.button("Analyze")

    if gaming_hours > 10:
        st.warning("Extreme gaming duration detected.")
    if sleep_hours < 4:
        st.warning("Severely low sleep detected.")

# ============================================
# MAIN ANALYSIS
# ============================================

if analyze:

    user_data = {
        "daily_gaming_hours": gaming_hours,
        "monthly_game_spending_usd": spending,
        "sleep_hours": sleep_hours,
        "exercise_hours_weekly": exercise_hours,
        "social_isolation_score": social_isolation
    }

    addiction_input = build_feature_dataframe(user_data, addiction_features)
    strain_input = build_feature_dataframe(user_data, strain_features)

    addiction_pred = addiction_model.predict(addiction_input)[0]
    strain_pred = strain_model.predict(strain_input)[0]

    addiction_label, addiction_msg = interpret_risk(addiction_pred)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Addiction Risk", addiction_label)

    with col2:
        st.metric("Eye Strain Risk", "Yes" if strain_pred[0]==1 else "No")

    with col3:
        st.metric("Back/Neck Pain Risk", "Yes" if strain_pred[1]==1 else "No")

    st.markdown("---")

    # st.subheader("Risk Interpretation")
    # st.info(addiction_msg)

    # st.write("Raw Prediction:", addiction_pred)
    # st.write("Prediction Type:", type(addiction_pred))
    # def interpret_addiction_risk(prediction):
    #     pred = str(prediction).lower()

    #     if "low" in pred or pred == "0":
    #         return "Low", "green"
    #     elif "moderate" in pred or pred == "1":
    #         return "Moderate", "orange"
    #     elif "high" in pred or pred == "2":
    #         return "High", "red"
    #     else:
    #         return "Unknown", "gray"
    # risk_label, risk_color = interpret_addiction_risk(addiction_pred)
    # st.metric("Addiction Risk Level", risk_label)

    def interpret_addiction_risk(prediction):
        pred = str(prediction).strip().lower()

        if pred == "low":
            return "Low", "green", "Minimal behavioral risk."
        
        elif pred == "moderate":
            return "Moderate", "orange", "Noticeable behavioral dependence developing."
        
        elif pred == "high":
            return "High", "red", "Strong signs of addiction-related behavior."
        
        elif pred == "severe":
            return "Severe", "darkred", "Critical addiction risk. Immediate lifestyle intervention recommended."
        
        else:
            return "Unknown", "gray", "Model returned an unexpected value."

    risk_label, risk_color, risk_text = interpret_addiction_risk(addiction_pred)
    st.metric("Addiction Risk Level", risk_label)
    st.caption(risk_text)


    # Spirit Animal Section
    health_risk_score = int(strain_pred[0]) + int(strain_pred[1])
    traits = build_user_traits(
        gaming_hours,
        sleep_hours,
        exercise_hours,
        social_isolation,
        health_risk_score
    )

    matches = match_spirit_animal(traits)

    st.subheader("Spirit Animal Archetype")
    for match in matches:
        st.markdown(f"### {match['animal']} ({match['score']})")
        st.write(match["archetype"])
        st.write(match["description"])

    st.subheader("Behavioral Radar Profile")
    fig = plot_radar(traits)
    st.pyplot(fig)

    st.subheader("Recommendations")

    if addiction_label == "High":
        st.warning("Reduce gaming hours and improve sleep hygiene.")
    elif addiction_label == "Moderate":
        st.info("Monitor gaming behavior and maintain balance.")
    else:
        st.success("Healthy behavioral patterns detected.")

st.markdown("---")
st.markdown("Developed by Tejas Alte")
