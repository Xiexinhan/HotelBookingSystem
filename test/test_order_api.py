import unittest
from flask import Flask
from flask_restful import Api
from app.contorllers.orders_controller import OrderResource
from app import create_app

class OrderApiTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_name_not_capitalized(self):
        #Error captialized
        response = self.client.post('/api/orders', json={
            "id": "A0000001",
            "name": "melody holiday inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "TWD"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Name is not capitalized", response.get_json()["errors"])

    def test_name_not_english(self):
        #Error not english
        response = self.client.post('/api/orders', json={
            "id": "A0000001",
            "name": "Melody Holiday Inn台北",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "TWD"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Name contains non-English characters", response.get_json()["errors"])

    def test_invalid_currency(self):
        #error currency
        response = self.client.post('/api/orders', json={
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1000,
            "currency": "EUR" 
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Currency format is wrong", response.get_json()["errors"])

    def test_valid_over_price(self):
        #over price
        response = self.client.post('/api/orders', json={
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 2100,  
            "currency": "TWD"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("Price is over 2000", response.get_json()['errors'])
    

    def test_valid_usd_usd_currency(self):
        #currency USD
        response = self.client.post('/api/orders', json={
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 100,  
            "currency": "USD"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()["order"]
        self.assertEqual(data["price"], 3100) 
        self.assertEqual(data["currency"], "TWD")  

    def test_valid_twd_currency(self):
        #currency TWD
        response = self.client.post('/api/orders', json={
            "id": "A0000001",
            "name": "Melody Holiday Inn",
            "address": {
                "city": "taipei-city",
                "district": "da-an-district",
                "street": "fuxing-south-road"
            },
            "price": 1900,  
            "currency": "TWD"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()["order"]
        self.assertEqual(data["price"], 1900) 
        self.assertEqual(data["currency"], "TWD")  

   

if __name__ == '__main__':
    unittest.main()
