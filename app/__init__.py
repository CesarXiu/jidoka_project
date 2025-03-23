from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes.web import main
    from app.routes.banda import banda_bp
    app.register_blueprint(main)
    app.register_blueprint(banda_bp)

    return app
