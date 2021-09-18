from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)
# run_with_ngrok(app)
model = pickle.load(open("model2.pkl", 'rb'))  # file path may be different

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model.predict(final_features)

    output=round(prediction[0],2)
    if prediction == 1:
        pred = "Your symptoms show Covid detection, please consult a Doctor."
    elif prediction == 0:
        pred = "You don't have Covid."
    output = pred
    return render_template('symptoms.html', prediction_text='COVID Results {}'.format(output))

@app.route('/xrays')
def xrays():
    return render_template('xray.html')
    
# @app.route('/results', methods=['POST'])
# def results():
#     data = request.get_json(force=True)
#     prediction=model.predict([np.array(list(data.values()))])

#     output=prediction[0]
#     # return jsonify(output)
#     return render_template('result.html', prediction=output)


if __name__ == "__main__":
    app.run()


