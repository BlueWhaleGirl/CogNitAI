# CogNitAI

CogNitAI is a machine learning–powered web application that predicts an individual’s susceptibility to cognitive decline using structured clinical and behavioral inputs. The system combines a supervised learning model with an interactive questionnaire-based interface to deliver real-time risk assessment through a Flask web application.

---

## 🧠 Overview

Early detection of cognitive decline is critical for timely intervention. CogNitAI explores how machine learning can support this process by analyzing patient-like clinical features and generating a risk prediction based on learned patterns in the data.

The project demonstrates an end-to-end machine learning pipeline, from data preprocessing and exploratory analysis to model training and deployment in a web environment.

---

## 🚀 Features

- Interactive web-based questionnaire for user input  
- Machine learning model trained on clinical-style data  
- Real-time risk prediction  
- Clean Flask-based backend and templated frontend  
- Integrated data preprocessing and feature engineering pipeline  

---

## 📊 Model Development & Visualizations

All exploratory data analysis, preprocessing, and model training were conducted in `model.ipynb`.

The notebook includes:
- Feature distribution analysis  
- Correlation heatmaps  
- Class imbalance visualization  
- Model evaluation and performance comparison  

These insights informed feature selection and model optimization prior to deployment.

---

## 🛠 Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas / NumPy  
- HTML / CSS (Jinja templates)  
- Jupyter Notebook  

---

## 📁 Project Structure

CogNitAI_aub/
│
├── app.py                  # Flask backend
├── model.ipynb             # Model training + EDA
├── models/                 # Saved ML models
├── data/                   # Dataset files
├── static/                 # CSS / assets
├── templates/              # HTML pages
└── requirements.txt

---

## ⚙️ How to Run Locally

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/CogNitAI.git

# Enter directory
cd CogNitAI

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
