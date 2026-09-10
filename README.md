# 🎮 Gamer Persona AI

**Predicting player personas and gaming addiction risk using behavioral
analytics and machine learning.**

## 🌐 Live Demo

-   Streamlit:
    https://gamerpersona-ai-wgot23xfyrhfsu2rgmuv3u.streamlit.app
-   Kaggle Notebook:
    https://www.kaggle.com/code/tejace/gamer-behavior-analysis-addiction-risk-prediction

------------------------------------------------------------------------

## 📌 Overview

Gamer Persona AI is an end-to-end machine learning project that analyzes
player behavior and predicts a user's gaming persona from gameplay
habits, spending patterns, session frequency, and social gaming
behavior.

This project demonstrates the complete ML lifecycle:

-   Exploratory Data Analysis (EDA)
-   Feature Engineering
-   Model Training & Evaluation
-   Model Serialization using Joblib
-   Interactive Deployment with Streamlit

------------------------------------------------------------------------

## ✨ Features

-   🎯 Real-time gamer persona prediction
-   ⚡ Interactive Streamlit web application
-   📊 Behavioral analytics & gameplay insights
-   🧠 Machine learning inference using Scikit-learn
-   📱 Responsive interface for desktop & mobile

------------------------------------------------------------------------

## 🧠 Machine Learning Pipeline

Raw Dataset → Data Cleaning → Feature Engineering → Model Training →
Joblib Model → Streamlit Deployment

------------------------------------------------------------------------

## 📊 Input Variables

The model analyzes behavioral signals including:

-   Gaming Hours
-   Preferred Genre
-   Platform
-   Session Frequency
-   Spending Behavior
-   Social Gaming Activity
-   Age & Demographic Features

The deployment uses the same preprocessing pipeline as the training
notebook to ensure consistent predictions.

------------------------------------------------------------------------

## 🛠 Tech Stack

  Category           Technology
  ------------------ ---------------
  Frontend           Streamlit
  Language           Python
  Machine Learning   Scikit-learn
  Data Processing    Pandas, NumPy
  Visualization      Matplotlib
  Model Storage      Joblib
  Version Control    Git & GitHub

------------------------------------------------------------------------

## 📁 Project Structure

``` text
gamerpersona-ai/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── gamer_behavior.csv
│
└── notebook/
    └── gamer_behavior_analysis.ipynb
```

------------------------------------------------------------------------

## ⚙️ Installation

Clone the repository:

``` bash
git clone https://github.com/YOUR_USERNAME/gamerpersona-ai.git
cd gamerpersona-ai
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run the application:

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 📦 Requirements

``` txt
streamlit
pandas
numpy
joblib
matplotlib
scikit-learn
```

------------------------------------------------------------------------

## 🚀 Future Improvements

-   LLM-powered personalized recommendations
-   SHAP model explainability
-   User authentication
-   Cloud database integration
-   Interactive analytics dashboard

------------------------------------------------------------------------

## 👨‍💻 Author

**Tejas Alte**

-   Kaggle:
    https://www.kaggle.com/code/tejace/gamer-behavior-analysis-addiction-risk-prediction

------------------------------------------------------------------------

## 📄 License

This project is intended for educational and portfolio purposes.
