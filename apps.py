from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model_heart')

labels = [
    "Enter Your Age", "Male Or Female [1/0]", "Enter Value of CP", "Enter Value of trestbps",
    "Enter Value of chol", "Enter Value of fbs", "Enter Value of restecg", "Enter Value of thalach",
    "Enter Value of exang", "Enter Value of oldpeak", "Enter Value of slope", "Enter Value of ca",
    "Enter Value of thal"
]

@app.route('/')
def index():
    return render_template('predicts.html', labels=labels)

@app.route('/predicts')  # Route for rendering the prediction form
def predicts():
    return render_template('predicts.html', labels=labels)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting input values from the form
        features = [
            int(request.form['enter_your_age']),
            int(request.form['male_or_female_[1/0]']),
            int(request.form['enter_value_of_cp']),
            int(request.form['enter_value_of_trestbps']),
            int(request.form['enter_value_of_chol']),
            int(request.form['enter_value_of_fbs']),
            int(request.form['enter_value_of_restecg']),
            int(request.form['enter_value_of_thalach']),
            int(request.form['enter_value_of_exang']),
            float(request.form['enter_value_of_oldpeak']),
            int(request.form['enter_value_of_slope']),
            int(request.form['enter_value_of_ca']),
            int(request.form['enter_value_of_thal'])
        ]

        prediction = model.predict(np.array([features]))

        if prediction == 0:
            result_message = "You do not have heart disease."
        else:
            result_message = "You have heart disease. Please consult a doctor."

        # Render the prediction result in predicts.html
        return render_template('predicts.html', labels=labels, result=result_message)

    except Exception as e:
        print(str(e))
        return render_template('predicts.html', labels=labels, result="Error occurred. Please check your input.")

if __name__ == '__main__':
    app.run(debug=True)
