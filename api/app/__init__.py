from flask import Flask
from response import response_success
from time import time

from exception import exception
from .user_app import user_bp
from .post_app import post_bp

app = Flask(__name__)
app.register_blueprint(exception)
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(post_bp, url_prefix='/post')


@app.route('/')
def hello_world():
    return response_success('success', int(round(time() * 1000)))


if __name__ == '__main__':
    app.run(debug=True)
