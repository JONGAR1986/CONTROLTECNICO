from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Lista en memoria para guardar ubicaciones
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

@app.route('/mapa')
def mostrar_mapa():
    return render_template('mapa.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
