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
TEST_NAME = "PruebaRegistroMascota"
BASE_DIR = "Capturas"
TEST_DIR = os.path.join(BASE_DIR, TEST_NAME)

# ===== Crear carpetas si no existen =====
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

# ===== Función para guardar capturas =====
def screenshot(driver, name):
    filename = f"{TEST_NAME}_{name}.png"
    path = os.path.join(TEST_DIR, filename)
    driver.save_screenshot(path)
    print(f"📸 Captura guardada: {path}")

# ===== Credenciales de la página =====
EMAIL = "CorreoCorrecto@ejemplo.com"
PASSWORD = "contraseña123."

# ===== Ingreso a la página =====
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
    print("✅ Click en botón Iniciar Sesión")
    screenshot(driver, "02_click_iniciar_sesion")
except:
    print("❌ Error al hacer clic en Iniciar Sesión")

time.sleep(2)

# ===== Llenar formulario de login =====
try:
    wait = WebDriverWait(driver, 10)

    campo_email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    campo_email.clear()
    campo_email.send_keys(EMAIL)

    campo_password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    campo_password.clear()
    campo_password.send_keys(PASSWORD)

    print("✅ Datos de login ingresados")
    screenshot(driver, "03_campos_login")

except:
    print("⚠️ No fue posible completar el formulario")

# ===== Click en botón Ingresar =====
try:
    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bg-blue-500.text-white.p-2.w-full"))
    )
    boton.click()
    print("✅ Click en botón Ingresar")
    screenshot(driver, "04_click_ingresar")
except:
    print("❌ Error al hacer clic en Ingresar")

time.sleep(1)

# ===== Click en botón Apadrinamiento / Agregar Mascota =====
try:
    boton = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '➕ Agregar Mascota')]"))
    )
    boton.click()
    print("✅ Click en ➕ Agregar Mascota")
    screenshot(driver, "05_click_agregar_mascota")
except:
    print("⚠️ No fue posible abrir Apadrinamiento")

time.sleep(2)

# ===== Completar los campos de nueva mascota =====
try:
    driver.find_element(By.NAME, "nombre").send_keys("Black")
    driver.find_element(By.NAME, "raza").send_keys("Border Collie")
    driver.find_element(By.NAME, "descripcion").send_keys("Dolor de estómago")

    print("✅ Datos de la mascota ingresados")
    screenshot(driver, "06_datos_mascota")

except:
    print("❌ Error llenando datos de mascota")

# ===== Click en Guardar Mascota =====
try:
    driver.find_element(By.XPATH, "//button[contains(text(), 'Guardar')]").click()
    print("✅ Mascota agregada correctamente")
    screenshot(driver, "07_guardar_mascota")
except:
    print("⚠️ No fue posible guardar la mascota")

time.sleep(2)
