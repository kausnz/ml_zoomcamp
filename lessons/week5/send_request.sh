curl -X POST http://localhost:9696/predict
   -H 'Content-Type: application/json'
   -d '{ 
"tenure": 1,
"monthlycharges": 29.85,
"totalcharges": 29.85,
"gender": "female",
"seniorcitizen": 0,
"partner": "yes",
"dependents": "no",
"phoneservice": "no",
"multiplelines": "no_phone_service",
"internetservice": "dsl",
"onlinesecurity": "no",
"onlinebackup": "yes",
"deviceprotection": "no",
"techsupport": "no",
"streamingtv": "no",
"streamingmovies": "no",
"contract": "month-to-month",
"paperlessbilling": "yes",
"paymentmethod": "electronic_check"}'