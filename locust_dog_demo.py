#Locust file
import dog_api_util
from locust import HttpUser, task

from dog_user_taskset import DogUserTaskSet, DogUserSequentialTaskSet


class DogUser(HttpUser):

    host = "https://dog.ceo/api/"
    tasks = [DogUserTaskSet, DogUserSequentialTaskSet]
    def on_start(self):
        print("Start User Action")

    def on_stop(self):
        print("Ending User Action")



