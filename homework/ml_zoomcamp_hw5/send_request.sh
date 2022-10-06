host='localhost:9696'

curl -v -X POST http://${host}/predict -H 'Content-Type: application/json' -d '{"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}'