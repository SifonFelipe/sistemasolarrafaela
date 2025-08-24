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
