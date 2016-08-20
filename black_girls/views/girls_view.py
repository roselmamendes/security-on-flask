from flask import Response
import json

class GirlsView:
    @staticmethod
    def generator(method):
        if method == 'GET':
            return GirlsGetView()
        elif method == 'POST':
            return GirlsPostView()


class GirlsGetView:
    def get_response(self, data=None):
        return Response(json.dumps(data), status=200, mimetype='application/json')


class GirlsPostView:
    def get_response(self, data=None):
        return Response(json.dumps(data), status=201, mimetype='application/json')

