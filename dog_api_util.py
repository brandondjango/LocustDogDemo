#util for providing information to make Dog API calls
import json
import requests
import random
import json


class DogApiCaller:

    def __init__(self):
        with open('ListOfDogBreeds.json','r') as file:
            json_file_content = file.read()
        self.breed_list_json = json.loads(json_file_content)

    def make_request(self, url):
        response = requests.get(url)

    def get_breeds_list_response(self):
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        return response

    def get_full_breed_list(self):
        #breeds_response = self.get_breeds_list_response()
        #breed_json = breeds_response.json()
        breed_json = self.breed_list_json
        breeds_dict = breed_json['message']
        breeds_list = list(breed_json["message"].keys())
        for breed in breeds_list:
            if breeds_dict[breed]:
                sub_breed_list = breeds_dict[breed]
                breeds_list = breeds_list + sub_breed_list
        return breeds_list

    def build_random_dog_breed_request(self):
        random_breed = random.choice(self.get_full_breed_list())
        request_url = "breed/" + random_breed + "/images/random"
        return request_url




