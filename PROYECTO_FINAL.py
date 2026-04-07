import scraper
import creador_web

# Primero corre el que busca los datos
scraper.ejecutar_scraper()

# Después corre el que hace la webo 
creador_web.generar_web()

print("\n🚀 ¡TODO EL PROCESO TERMINADO CON ÉXITO!")