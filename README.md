# ExampleWebApp
An example web app used for testing FLCI builds/deploys.

This is a fully functional Flask app that does (almost) nothing! This app has been created for integration testing of the FLCI system itself. It has only one route that is either / or /index and all it does is to return "Hello World! " concatinated with a version number. This version number can either be supplied via environment var or can be hard coded inside the app (with env var having the precedence). 

It can be run either as a standalone app or a dockerized app.


## Running Standalone 
Please note that you will need to install virtualenv before proceeding.

```
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
python -u run.py
```

## Running via Docker
Please note that you will need to install docker before proceeding.

```
docker build example-app .
docker run -p 5000 example-app
```
