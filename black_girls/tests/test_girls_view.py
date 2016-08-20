import unittest
import json
from flask import Response
from black_girls.views.girls_view import GirlsView


class TestGirlsView(unittest.TestCase):
    def test_should_return_a_get_view_for_girls(self):
        girls_get_view = GirlsView.generator('GET')

        expected_resp = Response(json.dumps([{'name': 'qual'}]), status=200, mimetype='application/json')
        actual_resp = girls_get_view.get_response(data=[{'name': 'qual'}])

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
