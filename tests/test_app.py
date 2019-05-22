import unittest

from app.main import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False

        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_convert_gold_api(self):
        payload = {
            "amount" : 1
        }
        response = self.app.post("/convert/buy", json=payload)
        # should return success!
        self.assertEqual(response.status_code, 200)
        # should return expected json
        data = response.get_json()
        self.assertEqual(data["amount"], payload["amount"])
        self.assertEqual(data["price"], 627000)

    def test_convert_gold_api_with_zero(self):
        payload = {
            "amount" : 0
        }
        response = self.app.post("/convert/buy", json=payload)
        # should return success!
        self.assertEqual(response.status_code, 400)
        # should return expected json
        data = response.get_json()
        self.assertEqual(data, "amount cant be zero")

if __name__ == "__main__":
    unittest.main()
