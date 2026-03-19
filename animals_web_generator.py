import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

def show_animals():
    for animal in animals_data:
        name = animal.get("name")
        if name:
            print(f"Name: {name}")

        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            print(f"Diet: {diet}")

        locations = animal.get("locations", [])
        if locations:
            print(f"Location: {locations[0]}")

        type_ = animal.get("characteristics", {}).get("type")
        if type_:
            print(f"Type: {type_}")

        print()

