#!/usr/bin/env python

import requests

url = 'http://localhost:9696/predict'

# payload =  { 
#     "tenure": 1,
#     "monthlycharges": 29.85,
#     "totalcharges": 29.85,
#     "gender": "female",
#     "seniorcitizen": 0,
#     "partner": "yes",
#     "dependents": "no",
#     "phoneservice": "no",
#     "multiplelines": "no_phone_service",
#     "internetservice": "dsl",
#     "onlinesecurity": "no",
#     "onlinebackup": "yes",
#     "deviceprotection": "no",
#     "techsupport": "no",
#     "streamingtv": "no",
#     "streamingmovies": "no",
#     "contract": "month-to-month",
#     "paperlessbilling": "yes",
#     "paymentmethod": "electronic_check"
# }

payload = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

resp = requests.post(url, json=payload)
print(resp.json())