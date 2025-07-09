from jinja2 import Environment, FileSystemLoader
import json
import os

with open("planetas.json", "r", encoding="utf-8") as f:
    planetas = json.load(f)

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("planeta.html")

output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)

for clave, datos in planetas.items():
    rendered = template.render(planeta=datos)
    with open(f"{output_dir}/{clave}.html", "w", encoding="utf-8") as f:
        f.write(rendered)

print("sites generated!")
