# Lab 1
> Live demo [Here](https://serverlab1.herokuapp.com/)
## How to run via python:
- Install python3
- Install pip
- Create environment `python3 -m venv env`
- Activate environment `source ./env/bin/activate`
- Install packages `pip install -r requirements.txt`
- Run app `flask --app core run --host 0.0.0.0 -p 8080`

## How to run via docker:
- Install docker
- Install docker-compose
- Build image `docker build --build-arg PORT=8080 . -t application:latest`
- Build container `sudo docker-compose build`
- Run container `sudo docker-compose up`