# Linear regression

A simple example of how to make a linear regression in scikit-learn,
train a model and create and API endpoint to predict new points

## Prepare your environment

`docker-compose up`

This will launch a container which will serve an API endpoint

`localhost:8080`

## How to launch test

Connect to container

`docker exec -it <container_name> bash`

`pytest`

## How to generate data

The script that generate mock data it is in linear_regression folder

This will generate your mockup data
`python generate_data.py`

The next script will train our linear regression and save it in data folder
`python linear_regression.py`

## Todo
- [ ] Frontend to interact with API