import json
import unittest
from flask import Response
from black_girls import black_girls_app
from black_girls.black_girls_view import GirlsView


class TestGirlsView(unittest.TestCase):

    def tearDown(self):
        black_girls_app.girls = []

    def test_should_return_a_get_view_for_girls(self):
        black_girls_app.girls = [
            {'name': 'Nina', 'profissao': 'dev', 'github': 'nina99'}
        ]
        expected_resp = Response(
            json.dumps(
                [{'name': 'Nina', 'profissao': 'dev', 'github': 'nina99'}]),
            status=200, mimetype='application/json')

        girls_get_view = GirlsView.generator('GET')
        actual_resp = girls_get_view.get_response()

        self.assertEqual(expected_resp.status, actual_resp.status)
        self.assertEqual(expected_resp.data, actual_resp.data)
        self.assertEqual(expected_resp.mimetype, actual_resp.mimetype)

    def test_should_return_a_post_view_for_girls(self):
        girls_post_view = GirlsView.generator('POST')

        expected_resp = Response(json.dumps({'name': 'qual'}), status=201, mimetype='application/json')
        actual_resp = girls_post_view.get_response(data={'name': 'qual'})

        self.assertEqual(expected_resp.status, actual_resp.status)
        self.assertEqual(expected_resp.data, actual_resp.data)
        self.assertEqual(expected_resp.mimetype, actual_resp.mimetype)
