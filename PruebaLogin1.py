import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ===== Nombre de la prueba =====
TEST_NAME = "PruebaLoginFallido"
BASE_DIR = "Capturas"
TEST_DIR = os.path.join(BASE_DIR, TEST_NAME)

# ===== Creación segura de carpetas =====
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
    print(f"📁 Carpeta creada: {BASE_DIR}")
else:
    print(f"📁 Carpeta ya existente: {BASE_DIR}")

if not os.path.exists(TEST_DIR):
    os.makedirs(TEST_DIR)
    print(f"📁 Carpeta creada: {TEST_DIR}")
else:
    print(f"📁 Carpeta ya existente: {TEST_DIR}")

# ===== Función para capturas =====
def screenshot(driver, name):
    filename = f"{TEST_NAME}_{name}.png"
    path = os.path.join(TEST_DIR, filename)
    driver.save_screenshot(path)
    print(f"📸 Captura guardada: {path}")

# ===== Credenciales de Prueba =====
EMAIL = "CorreoNo@ejemplo.com"
PASSWORD = "contraseña"

# ===== Ingreso a la página =====
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:8000/")
time.sleep(2)
screenshot(driver, "01_inicio")

# ===== Click en el botón de Iniciar Sesión =====
try:
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-blue-500.text-white.rounded-full"))
    )
    boton.click()
    print("✅ Click en 'Iniciar Sesion'")
    screenshot(driver, "02_click_iniciar")

except Exception as e:
    print("❌ Error al hacer clic en el botón:", e)

time.sleep(2)

# ===== Llenar email y contraseña =====
try:
    wait = WebDriverWait(driver, 10)

    campo_email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    campo_email.clear()
    campo_email.send_keys(EMAIL)

    campo_password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    campo_password.clear()
    campo_password.send_keys(PASSWORD)

    print("✅ Credenciales ingresadas.")
    screenshot(driver, "03_llena_credenciales")

except:
    print("⚠️ No fue posible completar los campos.")

# ===== Click en Ingresar =====
try:
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-blue-500.text-white.p-2.w-full"))
    )
    boton.click()
    print("✅ Click en botón Ingresar")
    screenshot(driver, "04_click_ingresar")

except:
    print("❌ Error al hacer clic en el botón Ingresar")

time.sleep(2)
