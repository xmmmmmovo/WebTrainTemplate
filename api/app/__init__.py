from flask import Flask
from response import response_success
from time import time

from flask_redis import Redis

from exception import exception
from .user_app import user_bp
from .post_app import post_bp

r = Redis()

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://redis:6379/0'
app.register_blueprint(exception)
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(post_bp, url_prefix='/post')
r.init_app(app)


@app.route('/')
def hello_world():
    return response_success('success', int(round(time() * 1000)))


if __name__ == '__main__':
    app.run(debug=True)
