import numpy as np
import pandas as pd
import pickle
import os
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained machine learning model and the feature scaler
# 'rb' means 'read binary' mode, which is required for loading pickle files
model = pickle.load(open('rdf.pkl', 'rb'))
scaler = pickle.load(open('scale1.pkl', 'rb'))

# Displays the main home page when a user visits the root URL (e.g., http://localhost:5000/)
@app.route('/')
def home():
    return render_template('home.html')

# Displays the page containing the HTML form where users fill out their details
@app.route('/predict')
def predict():
    return render_template('input.html')

# Handles the incoming POST request data after the user clicks the submit button
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Step 1: Extract form inputs sent by the user and convert them all to floats
        Gender = float(request.form['Gender'])
        Married = float(request.form['Married'])
        Dependents = float(request.form['Dependents'])
        Education = float(request.form['Education'])
        Self_Employed = float(request.form['Self_Employed'])
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        Credit_History = float(request.form['Credit_History'])
        Property_Area = float(request.form['Property_Area'])
        
        # Step 2: Combine all inputs into a 2D list (the format expected by the scaler)
        features = [[
            Gender, Married, Dependents, Education, Self_Employed, 
            ApplicantIncome, CoapplicantIncome, LoanAmount, 
            Loan_Amount_Term, Credit_History, Property_Area
        ]]
        
        # Terminal Debugging: Print original data for monitoring
        print('\n==============================')
        print('Original Features')
        print(features)
        
        # Step 3: Scale the raw inputs so they match the format used during model training
        scaled = scaler.transform(features)
        print('\nScaled Features')
        print(scaled)
        
        # Step 4: Convert the scaled array into a pandas DataFrame with matching column headers
        data = pd.DataFrame(scaled, columns=[
            'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 
            'Loan_Amount_Term', 'Credit_History', 'Property_Area'
        ])
        print('\nDataFrame')
        print(data)
        
        # Step 5: Feed the data frame into the model to get a prediction
        prediction = model.predict(data)
        print('\nPrediction = ', prediction)
        
        # Step 6: Map the numerical prediction output (usually 1 or 0) to user-friendly text
        if prediction[0] == 1:
            result = "✅ Loan Approved"
        else:
            result = "❌ Loan Rejected"
            
        # Step 7: Pass the result string to 'output.html' to render the final response page
        return render_template('output.html', result=result)
        
    except Exception as e:
        # Safety Net: If something goes wrong (e.g., empty inputs, missing keys), show the error text
        return f"<h2>Error:</h2><pre>{e}</pre>"

# Start the Flask web application
if __name__ == '__main__':
    # Runs the app locally on port 5000 with debug mode active for instant code updates
    app.run(host='0.0.0.0', port=5000, debug=True)
