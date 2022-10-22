import bentoml

# for other io descriptors https://docs.bentoml.org/en/latest/reference/api_io_descriptors.html
from bentoml.io import NumpyNdarray

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5") # version 1
# model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5") # version 2
model_runner = model_ref.to_runner()
# dv = model_ref.custom_objects['dictVectorizer']

# this variable name is what we refer to when running `bentoml serve ...` to start the service
mlzoomcamp_homework = bentoml.Service("mlzoomcamp_homework", runners=[model_runner])


@mlzoomcamp_homework.api(input=NumpyNdarray(), output=NumpyNdarray())
async def classify(vector):
    # application_data = payload.dict()

    # note that we are vector-ising but not transforming to a dictionary afterwards.
    # the runner must be doing the to_dict(orient='records') internally. And also note
    # the feature_names are not passed either.
    # vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction[0])
    return prediction[0]
