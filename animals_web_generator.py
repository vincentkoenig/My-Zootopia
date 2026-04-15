import json
import requests

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("API_KEY")

URL = "https://api.api-ninjas.com/v1/animals"


def load_data(file_path):
    """Lädt JSON-Daten aus einer Datei."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def fetch_animals(animal_name):
    params = {'name': animal_name}
    response = requests.get(URL, params=params, headers={"X-Api-Key": api_key})
    return response.json()


def serialize_animal(animal):
    """Serialisiert ein einzelnes Tierobjekt in HTML."""
    output = '<li class="cards__item">\n'

    name = animal.get("name")
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    diet = animal.get("characteristics", {}).get("diet")
    if diet:
        output += f'    <strong>Diet:</strong> {diet}<br/>\n'

    locations = animal.get("locations", [])
    if locations:
        output += f'    <strong>Location:</strong> {locations[0]}<br/>\n'

    type_ = animal.get("characteristics", {}).get("type")
    if type_:
        output += f'    <strong>Type:</strong> {type_}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_html(animals, template_file, output_file):
    """Generiert die finale HTML-Datei basierend auf einer Vorlage."""
    # Vorlage lesen
    with open(template_file, "r") as f:
        template = f.read()

    # Tiere serialisieren
    animals_html = ''
    for animal in animals:
        animals_html += serialize_animal(animal)

    # Platzhalter ersetzen
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Datei schreiben
    with open(output_file, "w") as f:
        f.write(final_html)


def main():
    animals_data = fetch_animals("Fox")
    generate_html(animals_data, "animals_template.html", "animals.html")


if __name__ == "__main__":
    main()