from flask import Flask, request, jsonify
from datetime import datetime
import os  # Necesitamos importar os para obtener el puerto

app = Flask(__name__)

ubicaciones = []

@app.route('/', methods=['GET'])
def home():
    return 'Servidor OwnTracks activo'

@app.route('/ubicacion', methods=['POST'])
def recibir_ubicacion():
    data = request.get_json()
    data['timestamp'] = datetime.utcnow().isoformat()
    ubicaciones.append(data)
    print(data)  # Opcional: ver en consola
    return jsonify({"mensaje": "Ubicación recibida"}), 200

@app.route('/ver', methods=['GET'])
def ver_ubicaciones():
    return jsonify(ubicaciones)

# Agrega esto para escuchar en el puerto dinámico de Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Obtiene el puerto dinámico
    app.run(host="0.0.0.0", port=port)

