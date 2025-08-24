from jinja2 import Environment, FileSystemLoader
import json
import os
from pathlib import Path

def get_path_items(path):
    gallery_path = Path("./docs/static/") / path
    files = []

    for file in gallery_path.glob("*"):
        relative_path = file.relative_to(Path("./docs/"))
        files.append(str(relative_path))

    return files


with open("planetas.json", "r", encoding="utf-8") as f:
    planetas = json.load(f)

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("planeta.html")

output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)

for clave, datos in planetas.items():
    for media_obj in datos['todos_aportamos']:
        media_obj['archivos'] = get_path_items(media_obj['path'])

    rendered = template.render(planeta=datos)
    with open(f"{output_dir}/{clave}.html", "w", encoding="utf-8") as f:
        f.write(rendered)

print("sites generated!")
