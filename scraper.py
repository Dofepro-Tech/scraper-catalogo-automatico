import requests
from bs4 import BeautifulSoup
import csv
import os

# CONFIGURACIÓN
BUSQUEDA = "zapatillas"
URL = f"https://listado.mercadolibre.com.do/{BUSQUEDA}"
CARPETA_FOTOS = 'fotos_finales'
ARCHIVO_CSV = 'reporte_mercadolibre.csv'

if not os.path.exists(CARPETA_FOTOS):
    os.makedirs(CARPETA_FOTOS)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def ejecutar_scraper():
    print(f"🕵️‍♂️ Extrayendo datos...")
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('li', class_='ui-search-layout__item')
    
    datos = []
    for i, item in enumerate(items[:20]):
        try:
            titulo_tag = item.find('a', class_='poly-component__title')
            titulo = titulo_tag.text.strip() if titulo_tag else f"Producto_{i}"
            link = titulo_tag['href'] if titulo_tag else "#"
            precio = item.find('span', class_='andes-money-amount__fraction').text.strip()
            
            # Descargar Foto
            img_tag = item.find('img', class_='poly-component__picture')
            img_url = img_tag.get('data-src') or img_tag.get('srcset') or img_tag.get('src')
            if img_url:
                if ' ' in img_url: img_url = img_url.split(' ')[0]
                n_limpio = "".join([c for c in titulo if c.isalnum() or c==' ']).strip()[:30]
                ruta_foto = os.path.join(CARPETA_FOTOS, f"{n_limpio}.jpg")
                img_data = requests.get(img_url, headers=HEADERS).content
                with open(ruta_foto, 'wb') as f:
                    f.write(img_data)
            
            datos.append([titulo, precio, link])
            print(f"✅ Item #{i+1} OK")
        except: continue

    with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Producto', 'Precio', 'Enlace'])
        writer.writerows(datos)
    print("📊 Excel generado.")

if __name__ == "__main__":
    ejecutar_scraper()