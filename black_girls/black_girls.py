from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

app = Flask(__name__)
app.config.from_object(__name__)

girls = []

@app.route('/girls', methods = ['GET', 'POST'])
def all_girls():
    resp = 'Welcome'

    if request.method == 'GET':
        resp = jsonify(girls)
        resp.mimetype = 'application/json'

    if request.method == 'POST':
       girls.append(request.get_json(force=True))
       resp = jsonify(girls[-1])
       resp.status_code = 201
       resp.mimetype = 'application/json'

    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')
