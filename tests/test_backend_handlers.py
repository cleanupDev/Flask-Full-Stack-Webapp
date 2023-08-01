import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
#from app import create_app



class TestHandlers(unittest.TestCase):
    def setUp(self):
        # app = create_app()
        # Set up your test environment (e.g., create a test database, start your Flask app, etc.)
        # Example: Start a Flask test client
        #self.client = app.test_client()
        pass

    def tearDown(self):
        # Clean up your test environment (e.g., delete test database, stop the Flask app, etc.)
        pass

    

if __name__ == '__main__':
    unittest.main()
