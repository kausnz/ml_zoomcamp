## Homework

In this homework, we will use Credit Card Data from [the previous homework](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/04-evaluation/homework.md).


## Question 1

* Install Pipenv
* What's the version of pipenv you installed?
* Use `--version` to find out

```
➜  ml_zoomcamp_hw5 git:(main) ✗ which pipenv
/Library/Frameworks/Python.framework/Versions/3.10/bin/pipenv
➜  ml_zoomcamp_hw5 git:(main) ✗ pipenv --version
pipenv, version 2022.9.24
```

## Question 2

* Use Pipenv to install Scikit-Learn version 1.0.2
* What's the first hash for scikit-learn you get in Pipfile.lock?

Note: you should create an empty folder for homework
and do it there. 

First hash is:
```
08ef968f6b72033c16c479c966bf37ccd49b06ea91b765e1cc27afefe723920b
```

From:
```
        "scikit-learn": {
            "hashes": [
                "sha256:08ef968f6b72033c16c479c966bf37ccd49b06ea91b765e1cc27afefe723920b",
                "sha256:158faf30684c92a78e12da19c73feff9641a928a8024b4fa5ec11d583f3d8a87",
                "sha256:16455ace947d8d9e5391435c2977178d0ff03a261571e67f627c8fee0f9d431a",
                "sha256:245c9b5a67445f6f044411e16a93a554edc1efdcce94d3fc0bc6a4b9ac30b752",
                "sha256:285db0352e635b9e3392b0b426bc48c3b485512d3b4ac3c7a44ec2a2ba061e66",
                "sha256:2f3b453e0b149898577e301d27e098dfe1a36943f7bb0ad704d1e548efc3b448",
                "sha256:46f431ec59dead665e1370314dbebc99ead05e1c0a9df42f22d6a0e00044820f",
                "sha256:55f2f3a8414e14fbee03782f9fe16cca0f141d639d2b1c1a36779fa069e1db57",
                "sha256:5cb33fe1dc6f73dc19e67b264dbb5dde2a0539b986435fdd78ed978c14654830",
                "sha256:75307d9ea39236cad7eea87143155eea24d48f93f3a2f9389c817f7019f00705",
                "sha256:7626a34eabbf370a638f32d1a3ad50526844ba58d63e3ab81ba91e2a7c6d037e",
                "sha256:7a93c1292799620df90348800d5ac06f3794c1316ca247525fa31169f6d25855",
                "sha256:7d6b2475f1c23a698b48515217eb26b45a6598c7b1840ba23b3c5acece658dbb",
                "sha256:80095a1e4b93bd33261ef03b9bc86d6db649f988ea4dbcf7110d0cded8d7213d",
                "sha256:85260fb430b795d806251dd3bb05e6f48cdc777ac31f2bcf2bc8bbed3270a8f5",
                "sha256:9369b030e155f8188743eb4893ac17a27f81d28a884af460870c7c072f114243",
                "sha256:a053a6a527c87c5c4fa7bf1ab2556fa16d8345cf99b6c5a19030a4a7cd8fd2c0",
                "sha256:a90b60048f9ffdd962d2ad2fb16367a87ac34d76e02550968719eb7b5716fd10",
                "sha256:a999c9f02ff9570c783069f1074f06fe7386ec65b84c983db5aeb8144356a355",
                "sha256:b1391d1a6e2268485a63c3073111fe3ba6ec5145fc957481cfd0652be571226d",
                "sha256:b54a62c6e318ddbfa7d22c383466d38d2ee770ebdb5ddb668d56a099f6eaf75f",
                "sha256:b5870959a5484b614f26d31ca4c17524b1b0317522199dc985c3b4256e030767",
                "sha256:bc3744dabc56b50bec73624aeca02e0def06b03cb287de26836e730659c5d29c",
                "sha256:d93d4c28370aea8a7cbf6015e8a669cd5d69f856cc2aa44e7a590fb805bb5583",
                "sha256:d9aac97e57c196206179f674f09bc6bffcd0284e2ba95b7fe0b402ac3f986023",
                "sha256:da3c84694ff693b5b3194d8752ccf935a665b8b5edc33a283122f4273ca3e687",
                "sha256:e174242caecb11e4abf169342641778f68e1bfaba80cd18acd6bc84286b9a534",
                "sha256:eabceab574f471de0b0eb3f2ecf2eee9f10b3106570481d007ed1c84ebf6d6a1",
                "sha256:f14517e174bd7332f1cca2c959e704696a5e0ba246eb8763e6c24876d8710049",
                "sha256:fa38a1b9b38ae1fad2863eff5e0d69608567453fdfc850c992e6e47eb764e846",
                "sha256:ff3fa8ea0e09e38677762afc6e14cad77b5e125b0ea70c9bba1992f02c93b028",
                "sha256:ff746a69ff2ef25f62b36338c615dd15954ddc3ab8e73530237dd73235e76d62"
            ],
            "index": "pypi",
            "version": "==1.0.2"
        },
```

## Models

We've prepared a dictionary vectorizer and a model.

They were trained (roughly) using this code:

```python
features = ['reports', 'share', 'expenditure', 'owner']
dicts = df[features].to_dict(orient='records')

dv = DictVectorizer(sparse=False)
X = dv.fit_transform(dicts)

model = LogisticRegression(solver='liblinear').fit(X, y)
```

> **Note**: You don't need to train the model. This code is just for your reference.

And then saved with Pickle. Download them:

* [DictVectorizer](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework/dv.bin?raw=true)
* [LogisticRegression](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/cohorts/2022/05-deployment/homework/model1.bin?raw=true)

With `wget`:

```bash
PREFIX=https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/course-zoomcamp/cohorts/2022/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin
```


## Question 3

Let's use these models!

* Write a script for loading these models with pickle
* Score this client:

```json
{"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
```

What's the probability that this client will get a credit card? 

* 0.148 ⏪
* 0.391
* 0.601
* 0.993

If you're getting errors when unpickling the files, check their checksum:

```bash
$ md5sum model1.bin dv.bin
3f57f3ebfdf57a9e1368dcd0f28a4a14  model1.bin
6b7cded86a52af7e81859647fa3a5c2e  dv.bin
```

My code for Q3:

```
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

```



## Question 4

Now let's serve this model as a web service

* Install Flask and gunicorn (or waitress, if you're on Windows)
* Write Flask code for serving the model
* Now score this client using `requests`:

```python
url = "YOUR_URL"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
requests.post(url, json=client).json()
```

What's the probability that this client will get a credit card?

* 0.274
* 0.484
* 0.698
* 0.928 ⏪


## Docker

Install [Docker](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/05-deployment/06-docker.md). We will use it for the next two questions.

For these questions, we prepared a base image: `svizor/zoomcamp-model:3.9.12-slim`. 
You'll need to use it (see Question 5 for an example).

This image is based on `python:3.9.12-slim` and has a logistic regression model 
(a different one) as well a dictionary vectorizer inside. 

This is how the Dockerfile for this image looks like:

```docker 
FROM python:3.9.12-slim
WORKDIR /app
COPY ["model2.bin", "dv.bin", "./"]
```

We already built it and then pushed it to [`svizor/zoomcamp-model:3.9.12-slim`](https://hub.docker.com/r/svizor/zoomcamp-model).

> **Note**: You don't need to build this docker image, it's just for your reference.


## Question 5

Download the base image `svizor/zoomcamp-model:3.9.12-slim`. You can easily make it by using [docker pull](https://docs.docker.com/engine/reference/commandline/pull/) command.

So what's the size of this base image?

* 15 Mb
* 125 Mb ⏪
* 275 Mb
* 415 Mb

You can get this information when running `docker images` - it'll be in the "SIZE" column.


## Dockerfile

Now create your own Dockerfile based on the image we prepared.

It should start like that:

```docker
FROM svizor/zoomcamp-model:3.9.12-slim
# add your stuff here
```

Now complete it:

* Install all the dependencies form the Pipenv file
* Copy your Flask script
* Run it with Gunicorn 

After that, you can build your docker image.


## Question 6

Let's run your docker container!

After running it, score this client once again:

```python
url = "YOUR_URL"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
requests.post(url, json=client).json()
```

What's the probability that this client will get a credit card now?

* 0.289
* 0.502
* 0.769 ⏪
* 0.972


## Submit the results

* Submit your results here: https://forms.gle/jU2we8f9WeLgX3qa6
* You can submit your solution multiple times. In this case, only the last submission will be used 
* If your answer doesn't match options exactly, select the closest one


## Deadline

The deadline for submitting is **10 October 2022 (Monday), 23:00 CEST (Berlin time)**. 

After that, the form will be closed.
