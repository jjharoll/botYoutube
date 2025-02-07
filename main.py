import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Función para simular la reproducción del video
def simular_reproduccion(url, visitas):
    try:
        # Configurar el navegador
        options = webdriver.ChromeOptions()
        options.add_argument("--mute-audio")  # Silenciar el audio
        options.add_argument("--autoplay-policy=no-user-gesture-required")  # Permitir autoplay sin interacción del usuario
        options.add_argument("--start-maximized")  # Maximizar la ventana del navegador

        # Iniciar el navegador
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        for i in range(int(visitas)):
            print(f"Reproduciendo video {i + 1}...")
            driver.get(url)
            time.sleep(5)  # Esperar 5 segundos para que el video se cargue y comience a reproducirse
            print(f"Visita {i + 1} completada.")
            time.sleep(5)  # Esperar 5 segundos adicionales para simular la reproducción
            driver.refresh()  # Recargar la página para simular una nueva visita

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