#!/usr/bin/env python

import pickle
from flask import Flask, request, jsonify

# read the model and dv from file
model_file = 'model2.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
  model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
  dv = pickle.load(f_in)

print(f'Model and DV loaded successfully: dv={dv}, model={model}')


app = Flask('predict')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[:, 1]
    y = y_pred >= 0.5
    
    result = {
        'y_pred' : float(y_pred),
        'y': bool(y)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
