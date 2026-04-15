import requests

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("API_KEY")

URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    params = {'name': animal_name}
    response = requests.get(URL, params=params, headers={"X-Api-Key": API_KEY})
    return response.json()