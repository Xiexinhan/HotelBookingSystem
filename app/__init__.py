from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    api = Api(app)
    with app.app_context():
        from .contorllers.orders_controller import OrderResource
        api.add_resource(OrderResource,'/api/orders')

        return app