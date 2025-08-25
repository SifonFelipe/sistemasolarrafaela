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

Para achicar los videos, se usó lo que está en el script `achicar_videos.py`.

Para achicar las imágenes, se usó esto desde un shell de linux (a veces con más de una corrida, y tocando la extensión):

```bash
find . -name "*.jpg" | xargs mogrify -resize 50%
```
