from jinja2 import Environment, FileSystemLoader
import json
import os
from pathlib import Path
from natsort import natsorted

def get_path_items(path):
    gallery_path = Path("./docs/static/") / path
    file_list = gallery_path.glob("*")
    files = []

    for file in natsorted(file_list):
        relative_path = file.relative_to(Path("./docs/"))
        files.append(str(relative_path))

    return files


def get_prev_after_item(order, item):    
    item_idx = order.index(item)
    prev_item = order[item_idx-1] if item_idx > 0 else order[-1]
    next_item = order[item_idx+1] if len(order) > item_idx+1 else order[0]

    return {"next": next_item, "prev": prev_item}


with open("planetas.json", "r", encoding="utf-8") as f:
    planetas = json.load(f)

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("planeta.html")

output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)
planet_order = ['sol', 'mercurio', 'venus', 'tierra', 'marte',
                'jupiter', 'saturno', 'urano', 'neptuno']

for clave, datos in planetas.items():
    for media_obj in datos['todos_aportamos']:
        media_obj['archivos'] = get_path_items(media_obj['path'])

    planetas_alrededor = get_prev_after_item(planet_order, clave)
    datos["siguiente"] = planetas_alrededor["next"]
    datos["anterior"] = planetas_alrededor["prev"]

    rendered = template.render(planeta=datos)
    with open(f"{output_dir}/{clave}.html", "w", encoding="utf-8") as f:
        f.write(rendered)

print("sites generated!")
