#util for providing information to make Dog API calls
import json
import requests
import random

class DogApiBuilderUtil:

    def __init__(self):
        api_base_url = "https://dog.ceo/api/"


    @classmethod
    def build_random_dog_breed_request(cls):
        breeds_response = DogApiCaller.get_breeds_list()
        breed_json = breeds_response.json()
        breeds_dict = breed_json["message"]
        breeds_list = list(breed_json["message"].keys())
        random_breed = random.choice(breeds_list)

        if breeds_dict[random_breed]:
            sub_breed_list = list(breeds_dict[random_breed].keys())
            random_breed = random.choice(sub_breed_list)

        request_url = "https://dog.ceo/api/breed/" + random_breed + "/images/random"
        return request_url



class DogApiCaller:

    def __init__(self):
        pass

    @classmethod
    def make_request(cls, url):
        response = requests.get(url)

    @classmethod
    def get_breeds_list(cls):
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        return response

    @classmethod
    def make_random_breed_image_request(cls):
        random_dog_breed_request = DogApiBuilderUtil().build_random_dog_breed_request()
        cls.make_request(random_dog_breed_request)



dog_api_builder = DogApiBuilderUtil().build_random_dog_breed_request()
print(dog_api_builder)

