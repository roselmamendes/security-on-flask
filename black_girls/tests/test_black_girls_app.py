import unittest
import json
from black_girls import black_girls_app
import uuid
import base64

class TestBlackGirl(unittest.TestCase):

    def setUp(self):
        black_girls_app.app.testing = True
        self.app = black_girls_app.app.test_client()

    def tearDown(self):
        black_girls_app.girls = []

    def test_should_return_all_saved_girls(self):
        data = json.dumps(dict(id='1', name='Nina', profissao='dev', \
                                                         github='nina99'))
        resp = self.app.post('/girls', data=data)

        self.assertEqual(201, resp.status_code, resp.data)

        resp = self.app.get('/girls')

        actual_resp = json.loads(resp.data.decode('utf8'))
        expected_resp = [
            {'id': '1', 'name': 'Nina', 'profissao': 'dev', 'github': 'nina99'}
        ]

        self.assertEqual(200, resp.status_code)
        self.assertEqual(1, len(actual_resp), 'Return different than 1 element')
        self.assertEqual(expected_resp, actual_resp)

    def test_should_create_a_girl_record(self):
        expected_resp = json.dumps(dict(id='1', name='Nina', profissao='dev',
                                        github='nina99'))

        resp = self.app.post('/girls', data=expected_resp)

        actual_resp = json.loads(resp.data.decode('utf8'))

        self.assertEqual(201, resp.status_code, resp.data)
        self.assertEqual(json.loads(expected_resp), actual_resp)

    def test_girl_by_id_should_return_a_girl_dict(self):
        id1 = str(uuid.uuid4())
        id2 = str(uuid.uuid4())

        girl = json.dumps(
            dict(id=id1, name='Nina', profissao='dev', github='nina99'))
        girl2 = json.dumps(
            dict(id=id2, name='Roberta', profissao='tester', github='rob99'))

        resp = self.app.post('/girls', data=girl)
        resp = self.app.post('/girls', data=girl2)

        actual_girl = black_girls_app.girl_by_id(id1)
        actual_girl2 = black_girls_app.girl_by_id(id2)

        self.assertEqual('Nina', actual_girl.name)
        self.assertEqual('Roberta', actual_girl2.name)

    def test_should_return_a_girl_when_passing_a_token(self):
        id1 = str(uuid.uuid4())
        token = base64.b64encode(bytes(id1, 'utf-8'))

        girl = json.dumps(
            dict(id=id1, name='Nina', profissao='dev', github='nina99'))

        resp = self.app.post('/girls', data=girl)

        resp = self.app.get(
            '/girls/{}'.format(id1),
            headers={'Authorization': 'Basic {}'.format(token.decode('utf-8'))})

        self.assertEqual(200, resp.status_code, resp.data)

        actual_resp = json.loads(resp.data.decode('utf8'))
        self.assertEqual(json.loads(girl), actual_resp)

        self.assertEqual('Nina', actual_resp['name'])
