from flask import Flask
from flask import jsonify
from flask import request
import flask_login
import base64
import json

app = Flask(__name__)
app.config.from_object(__name__)

girls = []

#Authentication
login_manager = flask_login.LoginManager()

login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(girl_id):
    return girl_by_id(girl_id)

def girl_by_id(girl_id):
    for girl in girls:
        if girl.id == girl_id:
            return girl
    return None

@login_manager.request_loader
def request_loader(request):
    token = request.headers.get('Authorization')
    token = token.replace('Basic', '', 1) if token else ''
    id = decode_token(token)
    return girl_by_id(id)

def decode_token(token):
    return base64.b64decode(token).decode("utf-8")

@app.route('/girls/<string:id>', methods = ['GET'])
@flask_login.login_required
def get_girl(id):
    json_girl = mixin_to_json(girl_by_id(id))
    return jsonify(json_girl)

@app.route('/girls', methods = ['GET'])
def all_girls():
    resp = 'Welcome'
    json_girls = mixin_list_to_json_list(girls)
    resp = jsonify(json_girls)
    resp.mimetype = 'application/json'
    return resp

@app.route('/girls', methods = ['POST'])
def create_girl():
    user_json = request.get_json(force=True)

    user = json_to_mixin(user_json)
    girls.append(user)

    resp = jsonify(mixin_to_json(girls[-1]))
    resp.status_code = 201
    resp.mimetype = 'application/json'
    return resp


def json_to_mixin(user_json):
    user = User()
    user.id = user_json['id']
    user.github = user_json['github']
    user.name = user_json['name']
    user.profissao = user_json['profissao']
    return user


def mixin_list_to_json_list(mixin_list):
    json_list = []
    for mixin in mixin_list:
        json_list.append(mixin_to_json(mixin))

    return json_list

def mixin_to_json(usermixin):
    return {
        "id": usermixin.id,
        "name": usermixin.name,
        "github": usermixin.github,
        "profissao": usermixin.profissao
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
