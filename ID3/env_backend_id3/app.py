from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os

app = Flask(__name__, static_folder='frontend')
CORS(app)  # Habilita CORS para toda la aplicación

@app.route('/')
def serve_frontend():
    return "Hola Mundo"

@app.route('/save-drawing', methods=['POST'])
def save_drawing():
    data = request.json
    image_data = data['image'].split(",")[1]
    save_path = './img/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # Guarda la imagen en la carpeta 'img'
    file_path = os.path.join(save_path, "saved_drawing.png")
    with open(file_path, "wb") as fh:
        fh.write(base64.b64decode(image_data))
    return jsonify({"message": "Dibujo guardado con éxito"})

if __name__ == '__main__':
    app.run(debug=True)