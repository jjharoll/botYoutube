import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

# Función para simular la reproducción del video
def simular_reproduccion(url, visitas):
    try:
        # Configurar el navegador
        options = Options()
        options.add_argument("--mute-audio")  # Silenciar el audio
        options.add_argument("--autoplay-policy=no-user-gesture-required")  # Permitir autoplay sin interacción del usuario
        options.add_argument("--incognito")  # Modo incógnito
        options.add_argument("--disable-blink-features=AutomationControlled")  # Evitar detección de bot
        options.add_argument("--disable-extensions")  # Deshabilitar extensiones
        options.add_argument("--start-maximized")  # Maximizar ventana

        # Cambiar User-Agent para evitar detección
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0"
        ]
        options.add_argument(f"user-agent={random.choice(user_agents)}")

        # Iniciar el navegador
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        for i in range(int(visitas)):
            print(f"Reproduciendo video {i + 1}...")
            driver.get(url)

            time.sleep(random.randint(8, 12))  # Esperar para que la página cargue

            try:
                # Darle play al video manualmente con Selenium
                video_element = driver.find_element(By.TAG_NAME, "body")
                ActionChains(driver).send_keys(Keys.SPACE).perform()  # Presionar "espacio" para iniciar la reproducción

                # Esperar un tiempo aleatorio (simulando visualización real)
                tiempo_visualizacion = random.randint(45, 180)  # Simula vistas más naturales (YouTube suele contar >30s)
                print(f"Viendo video durante {tiempo_visualizacion} segundos...")
                time.sleep(tiempo_visualizacion)

            except Exception as e:
                print(f"No se pudo interactuar con el video: {e}")

            print(f"Visita {i + 1} completada.")

            # Limpiar caché y cookies antes de la siguiente iteración
            driver.delete_all_cookies()
            time.sleep(random.randint(5, 10))  # Espera antes de la siguiente visita

        driver.quit()
        messagebox.showinfo("Éxito", "Simulación completada.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

# Interfaz gráfica con Tkinter
def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Bot de Simulación de Visitas")
    ventana.geometry("400x200")

    # Etiqueta y campo para la URL
    tk.Label(ventana, text="URL del video:").pack(pady=5)
    url_entry = tk.Entry(ventana, width=50)
    url_entry.pack(pady=5)

    # Etiqueta y campo para el número de visitas
    tk.Label(ventana, text="Número de visitas:").pack(pady=5)
    visitas_entry = tk.Entry(ventana, width=20)
    visitas_entry.pack(pady=5)

    # Botón para iniciar la simulación
    tk.Button(ventana, text="Iniciar Simulación", command=lambda: simular_reproduccion(url_entry.get(), visitas_entry.get())).pack(pady=20)

    ventana.mainloop()

# Iniciar la interfaz gráfica
if __name__ == "__main__":
    iniciar_interfaz()
