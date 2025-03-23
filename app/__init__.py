from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.routes.web import main
    from app.routes.banda import banda_bp
    from app.routes.item import item

    app.register_blueprint(main)
    app.register_blueprint(banda_bp)
    app.register_blueprint(item)

    return app
