# Scraper y Catalogo Automatico

Proyecto en Python que extrae productos desde MercadoLibre, descarga sus imagenes principales y genera un catalogo HTML listo para revisión visual.

## Que hace

- Consulta resultados de productos usando Requests y BeautifulSoup.
- Extrae titulo, precio y enlace de cada item.
- Descarga imagenes a una carpeta local.
- Genera un archivo CSV con los datos recolectados.
- Produce una vista HTML simple para revisar el catalogo generado.

## Stack

- Python 3
- Requests
- BeautifulSoup4
- CSV
- HTML/CSS

## Archivos principales

- `scraper.py`: realiza la extracción principal.
- `creador_web.py`: genera la vista HTML del catalogo.
- `reporte_mercadolibre.csv`: salida tabular con los productos capturados.
- `tienda_automatica.html`: vista visual generada.

## Instalacion

```bash
pip install -r requirements.txt
```

## Uso

```bash
python scraper.py
python creador_web.py
```

Luego abre `tienda_automatica.html` en el navegador para revisar el catalogo.

## Nota

Este proyecto tiene fines educativos y de automatización ligera. Si se usa en producción, conviene agregar manejo de errores más estricto, rotación de agentes, persistencia más robusta y validación del HTML objetivo.