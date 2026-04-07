import csv

def generar_web():
    print("🏗️  Vistiendo la tienda con diseño Pro...")
    archivo_csv = 'reporte_mercadolibre.csv'
    archivo_html = 'tienda_automatica.html'
    
    # Diseño mejorado con Menú y Nombre
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Zapatillas Pro RD | Catálogo Automático</title>
        <style>
            :root { --primary: #1a237e; --accent: #27ae60; --bg: #f8f9fa; }
            body { font-family: 'Segoe UI', sans-serif; background: var(--bg); margin: 0; padding: 0; }
            
            /* Navegación y Header */
            nav { background: white; padding: 15px 50px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); position: sticky; top: 0; z-index: 1000; }
            .logo { font-size: 1.5rem; font-weight: bold; color: var(--primary); text-transform: uppercase; letter-spacing: 1px; }
            .menu a { text-decoration: none; color: #555; margin-left: 20px; font-weight: 500; transition: 0.3s; }
            .menu a:hover { color: var(--primary); }
            
            header { background: var(--primary); color: white; text-align: center; padding: 60px 20px; }
            
            /* Cuadrícula de productos */
            .container { max-width: 1200px; margin: -40px auto 40px; padding: 0 20px; }
            .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 30px; }
            
            .card { background: white; border-radius: 15px; padding: 20px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: 0.4s; border: 1px solid #eee; }
            .card:hover { transform: translateY(-10px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); }
            .card img { width: 100%; height: 200px; object-fit: contain; margin-bottom: 15px; }
            
            .price { color: var(--accent); font-weight: bold; font-size: 1.5rem; margin: 10px 0; }
            .btn { display: block; background: var(--primary); color: white; padding: 12px; text-decoration: none; border-radius: 8px; font-weight: bold; transition: 0.3s; }
            .btn:hover { background: #3949ab; }
        </style>
    </head>
    <body>
        <nav>
            <div class="logo">👟 ZapatillasPro RD</div>
            <div class="menu">
                <a href="#">Inicio</a>
                <a href="#">Catálogo</a>
                <a href="#">Contacto</a>
            </div>
        </nav>
        
        <header>
            <h1>Catálogo Inteligente de Zapatillas</h1>
            <p>Actualizado automáticamente desde el mercado líder</p>
        </header>

        <div class="container">
            <div class="grid">
    """

    cards = ""
    try:
        with open(archivo_csv, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, delimiter=';')
            for fila in reader:
                n_foto = "".join([c for c in fila['Producto'] if c.isalnum() or c==' ']).strip()[:30]
                cards += f"""
                <div class="card">
                    <img src="fotos_finales/{n_foto}.jpg" onerror="this.src='https://via.placeholder.com/200?text=Zapato'">
                    <h4 style="height:45px; overflow:hidden;">{fila['Producto']}</h4>
                    <p class="price">${fila['Precio']}</p>
                    <a href="{fila['Enlace']}" target="_blank" class="btn">Ver Oferta</a>
                </div>"""

        with open(archivo_html, 'w', encoding='utf-8') as f:
            f.write(html_template + cards + "</div></div></body></html>")
        print(f"✨ ¡Web profesional generada en: {archivo_html}!")
    except Exception as e:
        print(f"❌ Error leyendo el CSV: {e}")

if __name__ == "__main__":
    generar_web()