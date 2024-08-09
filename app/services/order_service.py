class OrderService:
    def process_order(self, data):
        transformed_data = self._transform_order(data)
        return {"message": "Order processed successfully!", "order": transformed_data}

    def _transform_order(self, order):
        if order['currency'] == 'USD':
            order['price'] *= 31  
            order['currency'] = 'TWD'
        return order
