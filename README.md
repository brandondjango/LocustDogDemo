# LocustDogDemo
This project is a learning project for Locust using the [Dog Api](https://dog.ceo/dog-api/breeds-list).

Please do not use this to actually load test their API.

## Requirements

Python(This project was made using version 3.11)
Dependencies in requirements.txt(install using pip)

To install dependencies after Python is installed:

    pip install -r requirements.txt

To confirm installation of locust(you may need to add Locust to your path):

    locust -V

## Run Project

To run the project use:

    locust.exe -f .\locust_dog_demo.py

This will start a server on your localhost(default port is 8089, http://0.0.0.0:8089).

From here you can choose your user max number of users and users spawn rate.

**KEEP THIS LOW. DO NOT RUN A DOS ATTACK ON THE DOG API**

Then start the test!

