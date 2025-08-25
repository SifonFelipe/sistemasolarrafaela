from jinja2 import Environment, FileSystemLoader
import json
import os
from pathlib import Path
from natsort import natsorted

def get_path_items(path):
    """
    This gets the files from a path and returns a list with them
    in a string format to later get the extension from the file
    """

    gallery_path = Path("./docs/static/") / path
    file_list = gallery_path.glob("*")
    files = []

    for file in natsorted(file_list):  # natsorted() to sort better
        relative_path = file.relative_to(Path("./docs/"))  # relative_to from the template
        files.append(str(relative_path))

    return files


def get_prev_after_item(order, item):
    """
    This gets the previous and next item from a list giving
    a existing value
    """
    
    item_idx = order.index(item)
    prev_item = order[item_idx-1] if item_idx > 0 else order[-1]
    next_item = order[item_idx+1] if len(order) > item_idx+1 else order[0]

    return {"next": next_item, "prev": prev_item}

# Get json with data of the planets
with open("planetas.json", "r", encoding="utf-8") as f:
    planetas = json.load(f)

# Get templates to fill
env = Environment(loader=FileSystemLoader("templates"))
planet_template = env.get_template("planeta.html")
idx_template = env.get_template("index.html")

# Create or set the output dir
output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)

planet_order = ['sol', 'mercurio', 'venus', 'tierra', 'marte',
                'jupiter', 'saturno', 'urano', 'neptuno']

# Populate planet template with the .json
try:
    for clave, datos in planetas.items():

        # Set paths of the files to show in the template
        for media_obj in datos['todos_aportamos']:
            media_obj['archivos'] = get_path_items(media_obj['path'])

        planetas_alrededor = get_prev_after_item(planet_order, clave)
        datos["siguiente"] = planetas_alrededor["next"]
        datos["anterior"] = planetas_alrededor["prev"]

        rendered = planet_template.render(planeta=datos)
        with open(f"{output_dir}/{clave}.html", "w", encoding="utf-8") as f:
            f.write(rendered)

    print("Planet templates generated!")
except:
    print("Error at generating planet templates")

# Populate index template
try:
    index_render = idx_template.render(planetas=planetas)
    with open(f"{output_dir}/index.html", "w", encoding="utf-8") as f:
        f.write(index_render)

    print("Index template generated!")
except:
    print("Error at generating index template")

print("Done!")
