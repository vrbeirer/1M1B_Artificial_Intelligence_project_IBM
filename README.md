# 🌱 Tree Plantation Tracker using AI

A simple yet powerful web application that uses Artificial Intelligence to improve the success of tree plantation initiatives. The system records plantation details, predicts tree survival rates, and learns from real outcomes to support data-driven environmental decision-making.

---

## 📌 Problem Overview

Tree plantation drives are widely conducted by schools, communities, NGOs, and local authorities. However, many of these efforts fail to create long-term impact because tree survival is rarely tracked or analyzed after planting. Decisions such as planting season, watering frequency, and plantation size are often made without learning from past data, leading to low survival rates and wasted resources.

This project addresses this gap by combining historical plantation data with machine learning to predict survival rates and continuously improve predictions over time.

---

## 💡 Solution Summary

The Tree Plantation Tracker allows users to:
- Record tree plantation details through a simple web form
- Store plantation data in a structured database
- Predict tree survival rate using AI
- Learn from actual survival outcomes to improve future predictions

The system uses a machine learning model trained on real plantation records. When sufficient data is not available, a rule-based fallback logic ensures meaningful predictions, making the application reliable even in early stages.

---

## 🤖 AI & Machine Learning Used

- **Machine Learning Model:** Random Forest Regressor  
- **AI Approach:** Supervised learning using historical survival data  
- **Features Used for Prediction:**
  - Number of trees planted
  - Watering frequency per week
  - Seasonal information (Summer, Monsoon, Winter)

As more records with actual survival rates are added, the model retrains and becomes more accurate over time.

---

## 🛠️ Technology Stack

- **Backend:** Python, Flask  
- **Machine Learning:** scikit-learn (Random Forest)  
- **Database:** SQLite  
- **Data Processing:** Pandas  
- **Frontend:** HTML, CSS  

---

## 🌍 Sustainable Development Goals (SDGs)

This project aligns with the following UN Sustainable Development Goals:

- **SDG 9:** Industry, Innovation and Infrastructure  
- **SDG 11:** Sustainable Cities and Communities  
- **SDG 13:** Climate Action  
- **SDG 15:** Life on Land  

---

## ✨ Key Features

- AI-based tree survival prediction  
- Automatic season detection from planting date  
- Rule-based fallback when training data is limited  
- Continuous learning from real outcomes  
- Simple and user-friendly interface  
- Lightweight and easy to deploy  

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/tree-plantation-tracker-ai.git
cd tree-plantation-tracker-ai
