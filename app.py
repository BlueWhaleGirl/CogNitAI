from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('models/k_nearest_neighbors_pipeline.sav')

expected_features = [
    'MCQ053', 'SLQ060', 'RIAGENDR', 'RIDAGEYR', 'RIDRETH3', 'INDHHIN2',
    'BPQ020', 'BPQ080', 'DIQ010', 'PAD680', 'CDQ001', 'DPQ020', 'MCQ080',
    'MCQ084', 'MCQ220', 'DBQ700'
]

@app.route('/', methods=['GET'])
def input_form():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = {}
    missing_fields = []
    error_message = None

    for feature in expected_features:
        val = request.form.get(feature)
        if val is None or val.strip() == '':
            missing_fields.append(feature)
        else:
            try:
                user_input[feature] = float(val)
            except ValueError:
                error_message = f"Invalid input for {feature}. Please enter a valid number."
                break

    if missing_fields:
        error_message = f"Missing input for fields: {', '.join(missing_fields)}. Please fill all fields."

    if error_message:
        return render_template('output.html', prediction=None, error=error_message)

    input_df = pd.DataFrame([user_input])
    result = model.predict(input_df)[0]
    prediction = 'Likely Cognitive Decline' if result == 1 else 'No Cognitive Decline'

    return render_template('output.html', prediction=prediction, error=None)

if __name__ == '__main__':
    app.run(debug=True)
