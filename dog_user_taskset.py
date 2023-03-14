from locust import TaskSet, constant, task, SequentialTaskSet, tag

import dog_api_util
import dog_events


class DogUserTaskSet(TaskSet):

    @task
    @tag('list')
    def breeds_list(self):
        with self.client.get("breeds/list/all") as response:
            if response.status_code == 200:
                dog_events.custom_locust_event.fire(i=1, j=2, req_id=1, message="Breed list fetch successful.")

    @task
    @tag('random_dog_request')
    def random_dog_request(self):
        dog_caller = dog_api_util.DogApiCaller()
        dog_request = dog_caller.build_random_dog_breed_request()
        self.client.get(dog_request)
        print("Getting Random Dog Image")


class DogUserSequentialTaskSet(SequentialTaskSet):
    @task
    def breeds_list(self):
        with self.client.get("breeds/list/all") as response:
            if response.status_code == 200:
                dog_events.custom_locust_event.fire(i=1, j=2, req_id=1, message="Breed list fetch successful.")

    @task
    def random_dog_request(self):
        dog_caller = dog_api_util.DogApiCaller()
        self.client.get(dog_caller.build_random_dog_breed_request())
        print("Getting Sequential Random Dog Image")
