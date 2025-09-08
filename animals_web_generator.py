import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

data = load_data('animals_data.json')


def build_animals_string(data):
    """Builds an HTML string with animal info"""
    output = ""
    for animal in data:
        name = animal.get("name", "")
        diet = animal.get("characteristics", {}).get("diet")
        location = animal.get("locations", [])
        location_str = location[0] if location else None
        type_ = animal.get("characteristics", {}).get("type")

        # HTML-Block für das Tier
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{name}</div>\n'
        output += '  <p class="card__text">\n'
        if diet:
            output += f'      <strong>Diet:</strong> {diet}<br/>\n'
        if location_str:
            output += f'      <strong>Location:</strong> {location_str}<br/>\n'
        if type_:
            output += f'      <strong>Type:</strong> {type_}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'
    return output

def generate_html(template_path, output_path, animals_string):
    """Replaces placeholder in template and writes new HTML"""
    with open(template_path, "r") as template_file:
        html_content = template_file.read()

    # Platzhalter ersetzen
    new_html = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_string)

    # Neue Datei schreiben
    with open(output_path, "w") as output_file:
        output_file.write(new_html)

if __name__ == "__main__":
    data = load_data("animals_data.json")
    animals_string = build_animals_string(data)
    generate_html("animals_template.html", "animals.html", animals_string)
    print("animals_template.html wurde erstellt. Öffne die Datei im Browser, um das Ergebnis zu sehen.")