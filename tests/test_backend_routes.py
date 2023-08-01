import unittest
import requests

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
from app import create_app



class TestRoutes(unittest.TestCase):
    def setUp(self):
        app = create_app()
        # Set up your test environment (e.g., create a test database, start your Flask app, etc.)
        # Example: Start a Flask test client
        self.client = app.test_client()

    def tearDown(self):
        # Clean up your test environment (e.g., delete test database, stop the Flask app, etc.)
        pass

    def test_ping_route(self):
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Pong!"})

    def test_login_route(self):
        # Write test cases for login route
        pass

    def test_register_route(self):
        pass

if __name__ == '__main__':
    unittest.main()
