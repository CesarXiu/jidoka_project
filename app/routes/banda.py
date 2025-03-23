from flask import Blueprint, jsonify
from app.services import iniciar_banda, obtener_banda

banda_bp = Blueprint('banda', __name__, url_prefix='/api')

@banda_bp.route('/iniciar_banda', methods=['POST'])
def iniciar():
    iniciar_banda()
    return jsonify({"mensaje": "Banda iniciada"})

@banda_bp.route('/obtener_banda', methods=['GET'])
def obtener():
    return jsonify(obtener_banda())

# main.py
from flask import Flask
from app.routes.banda import banda_bp

app = Flask(__name__)
app.register_blueprint(banda_bp)

if __name__ == '__main__':
    app.run(debug=True)