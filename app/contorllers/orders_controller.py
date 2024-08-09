from flask_restful import Resource
from flask import request, jsonify
from marshmallow import ValidationError
from app.sechemas.order_sechemas import OrderSchema
from app.services.order_service import OrderService

class OrderResource(Resource):
    def __init__(self):
        self.order_service = OrderService()

    def post(self):
        schema = OrderSchema()
        try:
            data = schema.load(request.json)
            result = self.order_service.process_order(data)
            return result, 200
        except ValidationError as e:
            first_error = next(iter(e.messages.values()))[0]
            return {'errors':first_error}, 400
        