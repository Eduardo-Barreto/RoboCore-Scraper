import unittest
from app import app


class TestHistory(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_history(self):
        response = self.app.get("/history/963")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("robotId", data)
        self.assertIn("name", data)
        self.assertIn("team", data)
        self.assertIn("category", data)
        self.assertIn("events", data)
