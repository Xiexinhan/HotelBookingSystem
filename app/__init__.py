from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    with app.app_context():
        from .api.orders import orders_bp
        app.register_blueprint(orders_bp,url_prefix = '/api/orders')

        return app