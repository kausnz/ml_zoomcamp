import bentoml
from bentoml.io import JSON

model_ref = bentoml.xgboost.get("credit_risk_model:latest")
model_runner = model_ref.to_runner()
dv = model_ref.custom_objects['dictVectorizer']

cred_risk_svc = bentoml.Service("credit_risk_classifier", runners=[model_runner])


@cred_risk_svc.api(input=JSON(), output=JSON())
def classify(application_data):
    vector = dv.transform(application_data)
    prediction = model_runner.predict.run(vector)
    print(prediction)

    result = prediction[0]

    if result > 0.5:
        return "DECLINED"
    elif result > 0.23:
        return "MAYBE"
    else:
        return "APPROVED"
