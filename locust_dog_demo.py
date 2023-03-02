#Locust file
import dog_api_util
from locust import HttpUser, task

class DogCaller(HttpUser):

    #def __init__(self):
    #    self.random_dog_breed_request = dog_api_util.DogApiBuilderUtil().build_random_dog_breed_request()

    @task
    def breeds_list(self):
        self.client.get("/breeds/list/all")

    #@task
    #def random_dog_request(self):
    #    self.client.get(self.random_dog_breed_request)
