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
output = ''
for animal in animals_data:
    output += '<li class="cards__item">'
    name = animal.get("name")
    if name:
        output += f"Name: {name}<br/>\n"

    diet = animal.get("characteristics", {}).get("diet")
    if diet:
        output += f"Diet: {diet}<br/>\n"

    locations = animal.get("locations", [])
    if locations:
        output += f"Location: {locations[0]}<br/>\n"

    type_ = animal.get("characteristics", {}).get("type")
    if type_:
        output += f"Type: {type_}<br/>\n"

    output += '</li>\n'

# Platzhalter ersetzen
html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Neue HTML-Datei speichern
with open('animals.html', 'w') as file:
    file.write(html_content)

print("animals.html wurde erstellt!")