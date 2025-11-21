from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenamiento en memoria de los datos de cada prueba
DATA_STORE = {}


@app.route('/set-datos/<test_name>', methods=['POST'])
def set_datos(test_name):
    """Recibe los datos generados por n8n para una prueba específica."""
    try:
        DATA_STORE[test_name] = request.json or {}
        return jsonify({
            "status": "ok",
            "test_name": test_name,
            "message": "Datos almacenados correctamente"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 400


@app.route('/get-datos/<test_name>', methods=['GET'])
def get_datos(test_name):
    """Devuelve los datos almacenados para la prueba indicada."""
    data = DATA_STORE.get(test_name)
    if data is None:
        return jsonify({
            "status": "error",
            "error": f"No hay datos disponibles para la prueba '{test_name}'. "
                     "Asegúrate de que n8n haya enviado primero un POST a /set-datos/{test_name}."
        }), 404
    return jsonify(data), 200


if __name__ == '__main__':
    # Servidor Flask escuchando en localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=False)
