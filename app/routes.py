from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/banda')
def banda():
    return render_template('banda.html')

@main.route('/reportes')
def botones():
    return render_template('reportes.html')

@main.route('/supervisor')
def supervisores():
    return render_template('supervisor.html')
