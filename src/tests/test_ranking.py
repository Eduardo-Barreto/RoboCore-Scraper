import unittest
from app import app


class TestRanking(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_ranking(self):
        response = self.app.get("/ranking/sumo-3kg")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("category", data)
        self.assertIn("ranking", data)

    def test_get_ranking_not_found(self):
        response = self.app.get("/ranking/invalid-category")
        data = response.get_json()

        self.assertEqual(response.status_code, 404)
        self.assertIn("error", data)
        self.assertIn("status_code", data)
