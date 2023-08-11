import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))
# from app import create_app
from models.user import User


class TestModels(unittest.TestCase):
    def setUp(self):
        self.test_user = User(
            id=1,
            username="testuser",
            password="testpassword",
            email="testemail",
            first_name="testfirst",
            last_name="testlast",
            created_at="2021-01-01",
            is_active=True,
            is_admin=False,
            is_verified=True,
        )

    def tearDown(self):
        # Clean up your test environment (e.g., delete test database, stop the Flask app, etc.)
        pass

    def test_to_dict(self):
        self.assertEqual(
            self.test_user.to_dict(),
            {
                "id": 1,
                "username": "testuser",
                "password": "testpassword",
                "email": "testemail",
                "first_name": "testfirst",
                "last_name": "testlast",
                "created_at": "2021-01-01",
                "is_active": True,
                "is_admin": False,
                "is_verified": True,
            },
        )


if __name__ == "__main__":
    unittest.main()
