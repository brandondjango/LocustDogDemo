from locust import TaskSet, constant, task, SequentialTaskSet

import dog_api_util


class DogUserTaskSet(TaskSet):

    @task
    def breeds_list(self):
        self.client.get("breeds/list/all")
        print("Getting Breed List")
    @task
    def random_dog_request(self):
        dog_caller = dog_api_util.DogApiCaller()
        self.client.get(dog_caller.build_random_dog_breed_request())
        print("Getting Random Dog Image")


class DogUserSequentialTaskSet(SequentialTaskSet):
    @task
    def breeds_list(self):
        self.client.get("breeds/list/all")
        print("Getting Sequential Breed List")
    @task
    def random_dog_request(self):
        dog_caller = dog_api_util.DogApiCaller()
        self.client.get(dog_caller.build_random_dog_breed_request())
        print("Getting Sequential Random Dog Image")
