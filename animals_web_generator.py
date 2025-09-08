import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

data = load_data('animals_data.json')

def print_animals(data):
    """Iterates through animals and prints selected fields"""
    output = ""
    for animal in data:
        # append information to each string
        output += '<li class="cards__item">'
        if "name" in animal:
            output += f"Name: {animal['name']}<br/>\n"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}<br/>\n"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += "</li>"
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
    animals_string = print_animals(data)
    generate_html("animals_template.html", "animals.html", animals_string)
    print("animals_template.html wurde erstellt. Öffne die Datei im Browser, um das Ergebnis zu sehen.")