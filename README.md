# ExampleWebApp
an example web app used for testing FLCI builds/deploys

This is a fully functional FLask app that does nothing (well almost!). We have created this app for integration test of end to end functions. It has only one route that is either / or /index and all it does is to return "Hello World! " concatinated with a version number. This version number can either be supplied via environment var or can be hard coded inside the app (with env var having the precedence). 

It can be run either as a standalone app by issuing - 

```
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
python -u run.py
```

(of course creating the virtualenv and installing required packages are one of things and not to be done next time)

Or you can make a docker image using the Dockerfile provided and deploy a container based on that image. 

```
docker build example-app .
docker run -p 5000 example-app
```

It should be treated only as an example purpose app and not ready for any kind of production work.
