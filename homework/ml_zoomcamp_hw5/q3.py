#!/usr/bin/env python

import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
  model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
  dv = pickle.load(f_in)

print(f'Model and DV loaded successfully: dv={dv}, model={model}')

def predict():
    client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
    
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[:, 1]
    y = y_pred >= 0.5
    
    result = {
        'y_pred' : y_pred,
        'y': bool(y)
    }
    return result

print(predict())