import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datos import obtener_datos

# ===== Nombre de la prueba =====
TEST_NAME = "PruebaAdopcion"

# ===== Crear carpetas =====
# ===== Crear carpetas =====
BASE_DIR = "Capturas"
TEST_NAME = "PruebaAdopcion"
TEST_DIR = os.path.join(BASE_DIR, TEST_NAME)

# ===== Datos dinámicos desde Flask/n8n =====
datos = obtener_datos('adoptar')
EMAIL = datos.get('email', "CorreoCorrecto@ejemplo.com")
PASSWORD = datos.get('password', "contraseña123.")
TELEFONO = datos.get('telefono', "3101234565")
DIRRECION = datos.get('dirrecion', "Calle 1i#12-12")
MOTIVO = datos.get('motivo', "Es muy lindo")
FECHA = datos.get('fecha', "21112025")
HORA = datos.get('hora', "1235p")


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



# ===== Datos del apadrinamiento =====






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

# ===== Click en Apadrinar =====
try:
    boton = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '🏡 Adoptar')]"))
    )
    boton.click()
    print("✅ Click en Adoptar")
    screenshot(driver, "05_click_Adoptar")

except:
    print("❌ Error al hacer clic en Adoptar")

time.sleep(2)

# ===== Llenar Adopcion =====
try:

    #Campo telefono
    
    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "telefono"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(TELEFONO)

    #Campo direccion

    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "direccion"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(DIRRECION)

    #Campo motivo

    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "motivo"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(MOTIVO)

    #Campo fecha
    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "fecha"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(FECHA)
    
     #Campo hora
    campo_nombre = wait.until(
        EC.presence_of_element_located((By.NAME, "hora"))
    )
    campo_nombre.clear()
    campo_nombre.send_keys(HORA)
    

    print("✅ Datos de Adopcion llenados")
    screenshot(driver, "06_llena_Adopcion")

except:
    print("⚠️ No fue posible llenar los datos")

# Click en Confirmar Apadrinamiento

boton = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Enviar Solicitud')]"))
    )
boton.click()

print("✅ Click en Apadrinar")
screenshot(driver, "07_click_Enviar_Solicitud")