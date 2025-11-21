import requests

def obtener_datos(test_name, base_url="http://localhost:5000"):
    """Obtiene datos dinámicos para la prueba desde el servidor Flask/n8n.

    :param test_name: nombre del test (endpoint configurado en Flask)
    :param base_url: URL base del servidor Flask
    :return: diccionario con los datos de prueba
    """
    url = f"{base_url}/get-datos/{test_name}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"⚠️ Error al obtener datos para {test_name} desde {url}: {e}")
        return {}
