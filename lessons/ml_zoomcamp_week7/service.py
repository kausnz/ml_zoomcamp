import bentoml

# for other io descriptors https://docs.bentoml.org/en/latest/reference/api_io_descriptors.html
from bentoml.io import JSON

# this is used for defining schemas for the incoming requests and perform validations as they come in.
from pydantic import BaseModel


class CreditApplication(BaseModel):
    seniority: int
    home: str
    time: int
    age: int
    marital: str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: int
    price: int


model_ref = bentoml.xgboost.get("credit_risk_model:latest")
model_runner = model_ref.to_runner()
dv = model_ref.custom_objects['dictVectorizer']

# this variable name is what we refer to when running `bentoml serve ...` to start the service
cred_risk_svc = bentoml.Service("credit_risk_classifier", runners=[model_runner])


@cred_risk_svc.api(input=JSON(pydantic_model=CreditApplication), output=JSON())
async def classify(payload: CreditApplication):
    application_data = payload.dict()

    # note that we are vector-ising but not transforming to a dictionary afterwards.
    # the runner must be doing the to_dict(orient='records') internally. And also note
    # the feature_names are not passed either.
    vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)

    result = prediction[0]

    if result > 0.5:
        return "DECLINED"
    elif result > 0.23:
        return "MAYBE"
    else:
        return "APPROVED"
