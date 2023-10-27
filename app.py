from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np

#app = Flask(__name__)
app = Flask(__name__, template_folder='template') 


model_file = open('Buyscomputer.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', hasil=0)

@app.route('/play', methods=['POST'])
def predict():
    age = float(request.form['age'])
    
    age_string = "Age"
    if age == 0.0:
        age_string = "Middle Aged"
    elif age == 1.0:
        age_string = "Senior"
    elif age == 2.0:
        age_string = "Youth"

        

    income_string = "Income"
    income = float(request.form['income'])
    if income == 0.0:
        income_string = "High"
    elif income == 1.0:
        income_string = "Low"
    elif income == 2.0:
        income_string = "Medium"
        
        
    student_string = "Student"
    student = float(request.form['student'])
    if student == 0.0:
        student_string = "No"
    elif student == 1.0:
        student_string = "Yes"
        
        
    creditrating_string = "Credit Rating"
    creditrating = float(request.form['creditrating'])
    if creditrating == 0.0:
        creditrating_string = "Excellent"
    elif creditrating == 1.0:
        creditrating_string = "Fair"
        
    x = np.array([[age, income, student, creditrating]])
    
    prediction = model.predict(x)
    output = round(prediction[0],0)
    if (output == 0):
        kelas = "Jangan AHHH"
    elif (output == 1):
        kelas = "Beli Donggg"
        
    return render_template('index.html',hasil=kelas, age=age_string, income=income_string, student=student_string, creditrating=creditrating_string)

if __name__ == '__main__':
    app.run(debug=True)

