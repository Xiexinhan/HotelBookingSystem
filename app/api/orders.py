from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService

order_bp = Blueprint('orders',__name__)

@orders_bp.route('',methods =['Post'])
def create_order():
    data = request.json
    errors = OrderService.validate_order(data)

    if errors: 
        return jsonify({'errors':errors}),400
    
    transformed_order = OrderService.transform_order(data)
    return jsonify(transformed_order),200