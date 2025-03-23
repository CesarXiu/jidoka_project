from flask import Blueprint, jsonify
from app.services.bandService import actualizar_item as actualizar_item_service
item = Blueprint('item', __name__, url_prefix='/api')

@item.route('/status/<int:posicion>/ok', methods=['PUT'])
def ok(posicion):
    try:
        return jsonify(actualizar_item_service(posicion, "ok")), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@item.route('/status/<int:posicion>/report', methods=['PUT'])
def trouble(posicion):
    try:
        return jsonify(actualizar_item_service(posicion, "report")), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@item.route('/status/<int:posicion>/release', methods=['PUT'])
def release(posicion):
    try:
        return jsonify(actualizar_item_service(posicion, "ok")), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400