import random
from flask import Flask, jsonify, request
from flask_httpauth import HTTPDigestAuth as RequestDigestAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key here'
auth = RequestDigestAuth()

users = {
    'vcu': 'rams'
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/pong', methods=['GET'])
@auth.login_required
def pong():
    pong = random.randint(0, 1000)

    return jsonify(str(pong)), 201


if __name__ == '__main__':
    app.run()
