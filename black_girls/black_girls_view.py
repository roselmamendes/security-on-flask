from flask import Response
import json
from black_girls import black_girls_app


class GirlsView:
    @staticmethod
    def generator(method):
        if method == 'GET':
            return GirlsGetView()
        elif method == 'POST':
            return GirlsPostView()


class GirlsGetView:
    def get_response(self):
        return Response(json.dumps(black_girls_app.girls), status=200,
                        mimetype='application/json')


class GirlsPostView:
    def get_response(self, data=None):
        return Response(json.dumps(data), status=201, mimetype='application/json')

