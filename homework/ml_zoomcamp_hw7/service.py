import bentoml

# for other io descriptors https://docs.bentoml.org/en/latest/reference/api_io_descriptors.html
from bentoml.io import NumpyNdarray

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5") # version 1
# model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5") # version 2
model_runner = model_ref.to_runner()

# this variable name is what we refer to when running `bentoml serve ...` to start the service
mlzoomcamp_homework = bentoml.Service("mlzoomcamp_homework", runners=[model_runner])


@mlzoomcamp_homework.api(input=NumpyNdarray(), output=NumpyNdarray())
async def classify(vector):
    prediction = await model_runner.predict.async_run(vector)
    print(prediction[0])
    return prediction[0]
