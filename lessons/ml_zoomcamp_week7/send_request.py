#!/usr/bin/env python

import requests

url = 'http://localhost:3000/classify'

customer = {
    "seniority": 10,
    "home": "owner",
    "time": 36,
    "age": 36,
    "marital": "married",
    "records": "no",
    "job": "freelance",
    "expenses": 75,
    "income": 0.0,
    "assets": 10000.0,
    "debt": 0.0,
    "amount": 1000,
    "price": 4400
}

resp = requests.post(url, json=customer)
print(resp.json())
