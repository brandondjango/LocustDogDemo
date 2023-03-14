# LocustDogDemo
This project is a learning project for Locust using the [Dog Api](https://dog.ceo/dog-api/breeds-list).

Please do not use this to actually load test their API.

## Requirements

Python(This project was made using version 3.11)
Locust(This project was made using version 2.15)

To install Locust, you can use the command:

    pip3 install locust

To confirm installation:

    locust -V

## Concepts

### Users

[Users Documentation](https://docs.locust.io/en/stable/api.html#user-class)

Users are the "locusts" that perform load tests in your locust test.

Users are assigned Tasks to perform. Over the course of a locust test, Users are spawned at a rate determined by the test runner, and Users will automatically select tasks to run.

Furthermore, Locust provides a HttpUser class and a FastHttpUser class.  These built in classes come with http clients that can make http calls for you. In addition, they support cookies, and therefore keeps the session between HTTP requests.

Within an HttpUser for example, you can perform a http call like so:

    client.get("samplecall")

