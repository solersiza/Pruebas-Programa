import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


# ===== Nombre de la prueba =====
TEST_NAME = "PruebaRegistro"

# ===== Crear carpetas =====
BASE_DIR = "Capturas"
TEST_NAME = "PruebaRegistro"
TEST_DIR = os.path.join(BASE_DIR, TEST_NAME)

# Verificar carpeta principal
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
    print(f"📁 Carpeta creada: {BASE_DIR}")
else:
    print(f"📁 Carpeta ya existente: {BASE_DIR}")

# Verificar carpeta de la prueba
if not os.path.exists(TEST_DIR):
    os.makedirs(TEST_DIR)
    print(f"📁 Carpeta creada: {TEST_DIR}")
else:
    print(f"📁 Carpeta ya existente: {TEST_DIR}")

# ===== Función para capturas =====
def screenshot(driver, name):
    file_name = f"{TEST_NAME}_{name}.png"
    file_path = os.path.join(TEST_DIR, file_name)
    driver.save_screenshot(file_path)
    print(f"📸 Captura guardada: {file_path}")


# ===== Credenciales para Registrar =====
NOMBRE = "Juan"
APELLIDO = "Perez"
EMAIL = "CorreoCorrecto@ejemplo.com"
PASSWORD = "contraseña123."

# ===== Ingreso a la pagina =====
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:8000/")
time.sleep(2)
wait = WebDriverWait(driver, 5)

screenshot(driver, "01_inicio")

# ===== Click en el botón de Registro =====
try:
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Registrarse')]"))
    )
    boton.click()
    print("✅ Se presionó el enlace 'Registrarse'.")
    screenshot(driver, "02_click_registrarse")

except:
    print("⚠️ No fue posible presionar el enlace 'Registrarse'.")

time.sleep(1)

# ===== Llenar campos =====
try:
    nombre_input = wait.until(EC.presence_of_element_located((By.ID, "nombre")))
    nombre_input.clear()
    nombre_input.send_keys(NOMBRE)

    apellido_input = wait.until(EC.presence_of_element_located((By.ID, "apellido")))
    apellido_input.clear()
    apellido_input.send_keys(APELLIDO)

    email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email_input.clear()
    email_input.send_keys(EMAIL)

    password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(PASSWORD)

    print("✅ Datos ingresados.")
    screenshot(driver, "03_llena_campos")

except:
    print("❌ Error al llenar los datos")

# ===== Click en Registrar =====
try:
    boton = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.w-full.px-4.py-2.bg-green-600.text-white.rounded-lg.hover\\:bg-green-700.transition")
    ))
    boton.click()
    print("✅ Click realizado correctamente en el botón de Registro")
    screenshot(driver, "04_click_registrar")

except:
    print("❌ Error al hacer clic en el botón Registrar")

time.sleep(2)
