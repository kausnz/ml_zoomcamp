## gunicorn

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

