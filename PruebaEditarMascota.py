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
TEST_NAME = "PruebaEditar"


# ===== Crear carpetas =====
BASE_DIR = "Capturas"
TEST_NAME = "PruebaEditar"
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

# ===== Credenciales =====
EMAIL = "CorreoCorrecto@ejemplo.com"
PASSWORD = "contraseña123."

# ===== Nuevos Valores =====
NOMBRE = 'Lorenzo'
RAZA = 'Lorito'
DESCRIPCION = 'Guapo'

# ===== Abrir navegador =====
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:8000/")
time.sleep(2)
screenshot(driver, "01_inicio")

# ===== Click en Iniciar Sesión =====
try:
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-blue-500.text-white.rounded-full"))
    )
    boton.click()
    print("✅ Click en Iniciar Sesión")
    screenshot(driver, "02_click_iniciar_sesion")
except Exception as e:
    print("❌ Error al hacer clic:", e)

time.sleep(2)

# ===== Llenar credenciales =====
try:
    wait = WebDriverWait(driver, 10)

    campo_email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    campo_email.clear()
    campo_email.send_keys(EMAIL)

    campo_password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    campo_password.clear()
    campo_password.send_keys(PASSWORD)

    print("✅ Credenciales ingresadas")
    screenshot(driver, "03_llena_credenciales")

except:
    print("⚠️ No fue posible completar las credenciales")

# ===== Click en Ingresar =====
try:
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-blue-500.text-white.p-2.w-full"))
    )
    boton.click()
    print("✅ Click en Ingresar")
    screenshot(driver, "04_click_ingresar")

except:
    print("❌ Error en botón Ingresar")

time.sleep(2)

#Click en Editar
try:
    boton = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(), 'Editar')]"))
    )
    boton.click()
    print("✅ Click en Editar")
    screenshot(driver, "05_click_Editar")

except :
    print("❌ Error:")

try:

    #Campo nombre
    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "nombre"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(NOMBRE)

    #Campo raza

    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "raza"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(RAZA)

    #Campo descripcion

    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "descripcion"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(DESCRIPCION)

    print("✅ Click en Actualizar")
    screenshot(driver, "06_Actualizacion_Datos")

except:
    print("⚠️ No fue posible Actualizar los datos")

# Click en el boton Actualizar

boton = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Actualizar')]"))
    )
boton.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


print("✅ Click en Actualizar")
screenshot(driver, "07_click_Actualizar")