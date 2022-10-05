## Running on a production-ready wsgi (Web Server Gateway Interface) server

Out flask app can run on gunicorn as below:
```
pip install gunicorn
gunicorn --bind 0.0.0.0:9696 predict:app
```
where *predict* is the app name hardcoded in the app.
gunicorn will only run on linux or mac. Not on windows. waitress is an alternative that will work on windows.
```
pip install waitress
waitress-serve --listen=0.0.0.0:9696 predict:app
```

## Pipenv

E.g.

`pipenv install numpy scikit-learn flask`

To activate this project's virtualenv, run `pipenv shell`.
Alternatively, run a command inside the virtualenv with `pipenv run`.

Generates two files viz Pipfile, Pipfile.lock
The anyone who checkout the code with those files in the dir can just run `pipenv install` to setup the environment.

To exit a pipenv, press CTRL + D

pipenv is only for isolating python dependencies. If your python program requires a dependency then we have to use docker.

## Dockerize the app

Build the Dockerfile

`docker build -t zoomcamp-test .`

Run the container

`docker run -it --rm -p 9696:9696 zoomcamp-test`


## AWS Elastic Beanstalk

`pipenv install awsebcli --dev`

`eb init -p docker -r ap-southeast-2 churn-serving`

`eb local run --port 9696`

`eb create churn-serving-env`

`eb terminate churn-serving-env`