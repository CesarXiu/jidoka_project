from flask import Blueprint, render_template, jsonify
from app.services.bandService import obtener_banda

main = Blueprint('main', __name__)

#@main.route('/obtener_banda', methods=['GET'])
#def obtener_banda():
#    return jsonify({"data": banda.obtener_productos()})


@main.route('/')
def home():
    return render_template('index.html')

@main.route('/banda')
def banda():
    productos = obtener_banda()
    return render_template('banda.html', productos=productos)

@main.route('/reportes')
def botones():
    productos = obtener_banda()
    return render_template('reportes.html',productos=productos)

@main.route('/supervisor')
def supervisores():
    productos = obtener_banda()
    return render_template('supervisor.html',productos=productos)
