# Smart Lender — Loan Approval Prediction System

An intelligent machine learning-powered web application that predicts loan approval eligibility based on an applicant's demographic profile, financial history, and income details.

The system leverages a **Random Forest Classifier** trained on historical loan application data to provide fast and consistent credit eligibility predictions through an intuitive Flask web interface.

---
## 👥 Project Development Team
* **Sathvika Kolamudi**  
* **Mungari Samuel Abhishek** 
* **Veera Lakshmi Malladi**

# 🚀 Features

- Machine Learning-based loan approval prediction
- Random Forest classification model
- Standardized feature preprocessing using StandardScaler
- Interactive Flask web application
- User-friendly loan application form
- Instant prediction results
- Lightweight and easy local deployment

---

# 🛠️ Tech Stack

## Backend
- Python
- Flask

## Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Random Forest Classifier
- StandardScaler

## Frontend
- HTML5
- CSS3

---

# 📂 Project Structure
- The actual project is inside 5. Project Development Phase folder named as 'smart_lender_project' Folder.

```text
smart_lender_project/
│
├── app.py                  # Flask application and routing logic
├── loan.ipynb              # Model training notebook
├── loan_prediction.csv     # Dataset used for model training
├── rdf.pkl                 # Trained Random Forest model
├── scale1.pkl              # Trained StandardScaler object
├── requirements.txt        # Project dependencies
│
├── templates/
│   ├── home.html           # Landing page
│   ├── input.html          # Loan application form
│   └── output.html         # Prediction result page
│
└── static/
    └── css/
        └── input.css       # Application stylesheet
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/s-ath-vika/Smart-Lender
cd - direct to the project folder named smart_lender_project inside 5. Project Development Phase folder
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Train the Model

Before launching the application, generate the machine learning model files.

1. Open **loan.ipynb**
2. Select the appropriate Python kernel.
3. Run all notebook cells.
4. The following files will be generated:

```
rdf.pkl
scale1.pkl
```

These serialized objects are required by the Flask application during prediction.

---

# ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

---

# 🌐 Access the Application

After the server starts successfully, open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📊 Model Workflow

```text
User Input
      │
      ▼
Feature Preprocessing
(StandardScaler)
      │
      ▼
Random Forest Classifier
      │
      ▼
Loan Approval Prediction
      │
      ▼
Display Result
```

---

# 📋 Input Features

The prediction model considers several applicant attributes, including:

- Gender
- Marital Status
- Dependents
- Education
- Employment Status
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

# 📈 Machine Learning Pipeline

1. Load dataset
2. Data preprocessing
3. Handle missing values
4. Feature encoding
5. Feature scaling
6. Train Random Forest Classifier
7. Serialize trained model
8. Deploy using Flask

---

# 📦 Dependencies

Major libraries used:

- Flask
- pandas
- numpy
- scikit-learn
- pickle

Install everything with:

```bash
pip install -r requirements.txt
```

---

# 📸 Application Screens

- Home Page
- Loan Application Form
- Prediction Result


---

# 📄 License

This project is intended for educational purpose and evaluation under SmartBridge Internship.