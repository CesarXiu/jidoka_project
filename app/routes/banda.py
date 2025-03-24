from flask import Blueprint, jsonify
from app.services.bandService import iniciar_banda, obtener_banda, detener_banda

banda_bp = Blueprint('banda', __name__, url_prefix='/api')

@banda_bp.route('/iniciar_banda', methods=['POST'])
def iniciar():
    iniciar_banda()
    return jsonify({"mensaje": "Banda iniciada"})

@banda_bp.route('/obtener_banda', methods=['GET'])
def obtener():
    return jsonify(obtener_banda())

@banda_bp.route('/detener_banda', methods=['POST'])
def detener():
    detener_banda()
    return jsonify({"mensaje": "Banda detenida"})