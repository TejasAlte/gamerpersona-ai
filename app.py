import pandas as pd
import altair as alt

import matplotlib.pyplot as plt
import numpy as np

from spirit_engine import find_spirit

import streamlit as st
from scoring import *
from personas import *

st.set_page_config(page_title="GamerPersona AI", layout="centered")

st.title("🎮 GamerPersona AI")
st.subheader("Discover Your Gamer Energy")

st.markdown("---")

daily_hours = st.slider("How many hours do you game daily?", 0, 16, 4)
years_gaming = st.slider("How many years have you been gaming?", 0, 15, 3)
spending = st.slider("Monthly gaming spending ($)", 0, 500, 50)

sleep_hours = st.slider("How many hours do you sleep?", 0, 12, 7)
sleep_quality = st.selectbox("Sleep Quality", ["Good", "Poor", "Very Poor"])

mood = st.selectbox("Your usual mood after gaming?", ["Neutral", "Anxious", "Sad"])
withdrawal = st.checkbox("Do you feel restless when not gaming?")
continued = st.checkbox("Do you continue gaming despite problems?")

isolation = st.slider("Social isolation level (1–10)", 1, 10, 3)
face_hours = st.slider("Face-to-face social hours per week", 0, 20, 5)

exercise = st.slider("Exercise hours per week", 0, 10, 3)



def plot_radar(intensity, sleep, emotion, social, discipline):
    
    categories = ['INTENSITY', 'SLEEP', 'EMOTION', 'SOCIAL', 'DISCIPLINE']
    values = [intensity, sleep, emotion, social, discipline]
    
    # Close shape
    values += values[:1]
    
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6.5,6.5), subplot_kw=dict(polar=True))
    
    # Background
    fig.patch.set_facecolor('#0B0F19')
    ax.set_facecolor('#0B0F19')
    
    # 🔥 REMOVE circular frame completely
    ax.spines['polar'].set_visible(False)
    
    # Remove default grid
    ax.grid(False)
    
    # Draw pentagon grid layers (subtle)
    for level in [20, 40, 60, 80, 100]:
        ax.plot(angles, [level]*len(angles),
                color='#1C2333',
                linewidth=0.8)
    
    # Outer pentagon boundary (softer)
    ax.plot(angles, [100]*len(angles),
            color='#2EE6A6',
            linewidth=1.8)
    
    # Main stat shape (softer neon)
    ax.plot(angles, values,
            linewidth=2.8,
            color='#3EF0B5')
    
    ax.fill(angles, values,
            color='#3EF0B5',
            alpha=0.20)
    
    # Category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories,
                       fontsize=11,
                       fontweight='bold',
                       color='#D6E4F0')
    
    # Remove radial ticks
    ax.set_yticklabels([])
    
    ax.set_ylim(0, 100)
    
    return fig


# def plot_radar(intensity, sleep, emotion, social, discipline):
    
#     categories = ['INTENSITY', 'SLEEP', 'EMOTION', 'SOCIAL', 'DISCIPLINE']
#     values = [intensity, sleep, emotion, social, discipline]
    
#     # Close the shape
#     values += values[:1]
    
#     angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
#     angles += angles[:1]
    
#     fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(polar=True))
    
#     # Dark gaming background
#     fig.patch.set_facecolor('#0B0F19')
#     ax.set_facecolor('#0B0F19')
    
#     # Remove default grid
#     ax.grid(False)
    
#     # Draw sharp pentagon grid layers
#     for level in [20, 40, 60, 80, 100]:
#         ax.plot(angles, [level]*len(angles),
#                 color='#1F2A44',
#                 linewidth=1)
    
#     # Outer boundary thick
#     ax.plot(angles, [100]*len(angles),
#             color='#00F5FF',
#             linewidth=2.5)
    
#     # Main stat shape
#     ax.plot(angles, values,
#             linewidth=3.5,
#             color='#00FFAA')
    
#     ax.fill(angles, values,
#             color='#00FFAA',
#             alpha=0.25)
    
#     # Category labels
#     ax.set_xticks(angles[:-1])
#     ax.set_xticklabels(categories,
#                        fontsize=12,
#                        fontweight='bold',
#                        color='white')
    
#     # Remove radial numbers
#     ax.set_yticklabels([])
    
#     ax.set_ylim(0, 100)
    
#     # Add center glow effect
#     ax.scatter(0, 0, s=200, color='#00FFAA', alpha=0.4)
    
#     return fig


# def plot_radar(intensity, sleep, emotion, social, discipline):
    
#     categories = ['INTENSITY', 'SLEEP', 'EMOTION', 'SOCIAL', 'DISCIPLINE']
#     values = [intensity, sleep, emotion, social, discipline]
    
#     # Close shape
#     values += values[:1]
    
#     angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
#     angles += angles[:1]
    
#     fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    
#     # Dark background
#     fig.patch.set_facecolor('#0E1117')
#     ax.set_facecolor('#0E1117')
    
#     # Remove circular grid
#     ax.grid(False)
    
#     # Draw pentagon grid manually
#     for i in range(20, 101, 20):
#         ax.plot(angles, [i]*len(angles), linestyle='dashed', linewidth=0.6)
    
#     # Draw main pentagon
#     # ax.plot(angles, values, linewidth=3)
#     # ax.plot(angles, values, linewidth=3, color='#00FFAA')
#     ax.fill(angles, values, alpha=0.4, color='#00FFAA')
#     ax.fill(angles, values, alpha=0.3)
    
#     # Labels
#     ax.set_xticks(angles[:-1])
#     ax.set_xticklabels(categories, fontsize=11)
    
#     ax.set_ylim(0, 100)
    
#     # Remove radial labels
#     ax.set_yticklabels([])
    
#     return fig


# def plot_radar(intensity, sleep, emotion, social, discipline):
    
#     categories = ['Intensity', 'Sleep', 'Emotion', 'Social', 'Discipline']
#     values = [intensity, sleep, emotion, social, discipline]
    
#     # Close the pentagon
#     values += values[:1]
    
#     angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
#     angles += angles[:1]
    
#     # fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
#     fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
#     fig.patch.set_facecolor('#0E1117')
#     ax.set_facecolor('#0E1117')

    
#     ax.plot(angles, values)
#     ax.fill(angles, values, alpha=0.25)
    
#     ax.set_xticks(angles[:-1])
#     ax.set_xticklabels(categories)
    
#     ax.set_ylim(0, 100)
    
#     return fig



if st.button("Reveal My Gamer Persona 🔮"):
    
    intensity = gaming_intensity(daily_hours, years_gaming, spending)
    sleep_score = sleep_balance(sleep_hours, sleep_quality)
    emotion = emotional_drift(mood, withdrawal, continued)
    social = social_energy(isolation, face_hours)
    discipline = life_discipline(exercise)
    
    balance = balance_index([intensity, sleep_score, emotion, social, discipline])
    
    persona = get_persona(intensity, sleep_score, emotion, social)

    st.markdown("---")
    st.header(persona)
    
    st.subheader(f"🌌 Your Gamer Balance Index: {round(balance,1)} / 100")
    
    st.write("### 🪞 Personalized Insight")

    insight = ""

    if intensity > 70:
        insight += "Your gaming intensity is high, suggesting strong immersion and engagement. "

    if sleep_score < 50:
        insight += "Your sleep balance appears strained, possibly due to late-night sessions. "

    if emotion > 60:
        insight += "Emotional drift signals that gaming may be influencing your mood cycles. "

    if social < 50:
        insight += "Your social energy suggests digital interaction may be replacing real-world connections. "

    if discipline < 50:
        insight += "Life discipline indicators show room for healthier routine alignment. "

    if insight == "":
        insight = "Your gaming habits appear relatively balanced with your real-life systems."

    st.write(insight)


    user_vector = [intensity, sleep_score, emotion, social, discipline]

    spirit_name, spirit_description = find_spirit(user_vector)

    st.markdown("---")
    st.header("🧬 Your Spirit Alignment")
    st.subheader(spirit_name)
    st.write(spirit_description)



    st.write("### 🎯 Your Energy Map")

    data = pd.DataFrame({
        'Category': ['Intensity', 'Sleep', 'Emotion', 'Social', 'Discipline'],
        'Score': [intensity, sleep_score, emotion, social, discipline]
    })

    chart = alt.Chart(data).mark_line(point=True).encode(
        x=alt.X('Category', sort=None),
        y=alt.Y('Score', scale=alt.Scale(domain=[0, 100]))
    )

    st.altair_chart(chart, use_container_width=True)

    st.write("### 🌌 Your Energy Pentagon")

    radar_chart = plot_radar(intensity, sleep_score, emotion, social, discipline)

    st.pyplot(radar_chart)

