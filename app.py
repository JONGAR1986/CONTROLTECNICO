from flask import Flask, request, jsonify
import os

app = Flask(__name__)

ubicaciones = []

@app.route('/', methods=['GET'])
def home():
    return 'Servidor OwnTracks activo'

@app.route('/ubicacion', methods=['POST'])
def recibir_ubicacion():
    data = request.get_json()
    ubicaciones.append(data)
    return jsonify({"mensaje": "Ubicación recibida"}), 200

@app.route('/ver', methods=['GET'])
def ver_ubicaciones():
    return jsonify(ubicaciones)

if __name__ == '__main__':
    # Usar el puerto de la variable de entorno PORT de Render
    port = int(os.environ.get("PORT", 5000))  # Si no está configurado, usará el puerto 5000
    app.run(host='0.0.0.0', port=port)
