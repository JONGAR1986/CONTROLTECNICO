from flask import Flask, request, jsonify
from datetime import datetime

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
