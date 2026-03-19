import json


# JSON-Datei laden
def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

# Template laden
with open('animals_template.html', 'r') as f:
    template = f.read()

# String mit Tierdaten erzeugen
animals_info = ""
for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    type_ = animal.get("characteristics", {}).get("type")

    if name:
        animals_info += f"Name: {name}\n"
    if diet:
        animals_info += f"Diet: {diet}\n"
    if locations:
        animals_info += f"Location: {locations[0]}\n"
    if type_:
        animals_info += f"Type: {type_}\n"

    animals_info += "\n"  # Leerzeile zwischen Tieren

# Platzhalter ersetzen
output_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

# Neue HTML-Datei speichern
with open('animals.html', 'w') as f:
    f.write(output_html)

print("animals.html wurde erstellt!")