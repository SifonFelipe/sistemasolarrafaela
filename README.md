# Web del sistema solar a escala de Rafaela

# Instalación

Requiere tener instalado [UV](https://docs.astral.sh/uv/guides/install-python/#installing-a-specific-version), para luego simplemente correr: 
```bash
uv sync
```

# Compilar y deployar el sitio

Para compilar el sitio, correr:

```bash
uv run site_generator.py
```

Esto deja los htmls compilados en el directorio `docs/`.

Para deployar esos htmls actualizados, simplemente pushear al branch `main` del repo.

# Otra info útil

Para achicar los archivos, se usó esto desde un shell de python (y teniendo instalado ffmpeg):

```python
def achicar(video_path):
    from os import system
    cmd = f"ffmpeg -ss 0:0 -i '{video_path}' -c:a copy -vcodec libx265 -crf 28 '{video_path.replace('.mp4','_small.mp4')}'"
    system(cmd)

def achicar_muchos(dir_path):
    from pathlib import Path
    for f in Path(dir_path).glob("*.*"):
        print(f)
        achicar(str(f))

achicar_muchos("./un_path_con_videos_dentro")
```
