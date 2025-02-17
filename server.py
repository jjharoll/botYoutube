from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import logging

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Configuración de variables
URL_VIDEO = "https://www.youtube.com/watch?v=oGyvaQr_FwU"
VISITAS = 250

# Función para simular la reproducción del video
def simular_reproduccion(url, visitas):
    try:
        logging.info("Iniciando simulación...")

        # Configurar Chrome en modo headless
        options = Options()
        options.add_argument("--headless")  # Modo sin interfaz gráfica
        options.add_argument("--disable-gpu")  # Deshabilitar GPU (necesario para headless en algunos sistemas)
        options.add_argument("--no-sandbox")  # Evitar problemas de permisos en entornos sin GUI
        options.add_argument("--disable-dev-shm-usage")  # Solucionar problemas de memoria en contenedores
        options.add_argument("--mute-audio")  # Silenciar el audio
        options.add_argument("--incognito")  # Modo incógnito
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")  # Evitar detección de bot
        options.add_argument("--window-size=1920,1080")  # Simular una pantalla real

        # Cambiar User-Agent aleatorio para evitar detección
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"
        ]
        options.add_argument(f"user-agent={random.choice(user_agents)}")

        # Ruta del chromedriver (ajustar según versión de Chrome)
        service = Service("/usr/bin/chromedriver")  # Cambiar si está en otra ubicación

        # Iniciar el navegador
        driver = webdriver.Chrome(service=service, options=options)

        for i in range(visitas):
            logging.info(f"Visita {i + 1}/{visitas} en proceso...")
            driver.get(url)
            time.sleep(random.randint(5, 10))  # Esperar para carga de la página

            try:
                # Simular interacción para que YouTube lo cuente como una vista válida
                video_element = driver.find_element(By.TAG_NAME, "body")
                ActionChains(driver).send_keys(Keys.SPACE).perform()  # Simular presionar "espacio"

                tiempo_visualizacion = random.randint(45, 180)  # Simula vistas realistas
                logging.info(f"Viendo video durante {tiempo_visualizacion} segundos...")
                time.sleep(tiempo_visualizacion)

            except Exception as e:
                logging.error(f"Error al interactuar con el video: {e}")

            # Limpiar caché y cookies para simular nuevos usuarios
            driver.delete_all_cookies()
            time.sleep(random.randint(5, 10))

        driver.quit()
        logging.info("Simulación completada con éxito.")
    
    except Exception as e:
        logging.error(f"Ocurrió un error durante la ejecución: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

# Ejecutar el script
if __name__ == "__main__":
    simular_reproduccion(URL_VIDEO, VISITAS)
