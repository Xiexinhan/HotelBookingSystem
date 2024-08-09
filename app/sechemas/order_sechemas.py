from marshmallow import Schema, fields, validates, ValidationError
import re

class AddressSchema(Schema):
    city = fields.Str(required=True)
    district = fields.Str(required=True)
    street = fields.Str(required=True)

class OrderSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    address = fields.Nested(AddressSchema, required=True)
    price = fields.Float(required=True)
    currency = fields.Str(required=True)

    @validates('name')
    def validate_name(self, value):

        if not re.match(r'^[A-Za-z ]+$', value):
            raise ValidationError('Name contains non-English characters')
        
        # 检查是否首字母大写
        if not re.match(r'^[A-Z][a-z]+(?: [A-Z][a-z]+)*$', value):
            raise ValidationError('Name is not capitalized')
    @validates('price')
    def validate_price(self,value):
        if value > 2000:
            raise ValidationError('Price is over 2000')
    
    @validates('currency')
    def validate_currency(self,value):
        if value not in ['TWD','USD']:
            raise ValidationError('Currency format is wrong')