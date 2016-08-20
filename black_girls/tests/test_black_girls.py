import unittest
import json
from black_girls import black_girls

class TestBlackGirl(unittest.TestCase):

    def setUp(self):
        black_girls.app.testing = True
        self.app = black_girls.app.test_client()

    def tearDown(self):
        black_girls.girls = []

    def test_should_return_all_saved_girls(self):
        data = json.dumps(dict(name='Nina', profissao='dev', github='nina99'))
        resp = self.app.post('/girls', data=data)

        self.assertEqual(201, resp.status_code, resp.data)

        resp = self.app.get('/girls')

        actual_resp = json.loads(resp.data.decode('utf8'))
        expected_resp = [
            {'name': 'Nina', 'profissao': 'dev', 'github': 'nina99'}
        ]

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(actual_resp), 'Return different than 1 element')
        self.assertEqual(expected_resp, actual_resp)

    def test_should_create_a_girl_record(self):
        data = json.dumps(dict(name='Nina', profissao='dev', github='nina99'))

        resp = self.app.post('/girls', data=data)

        actual_resp = json.loads(resp.data.decode('utf8'))

        self.assertEqual(201, resp.status_code, resp.data)
        self.assertEqual(json.loads(data), actual_resp)