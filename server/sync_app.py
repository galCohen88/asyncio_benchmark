from flask import Flask
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
app = Flask(__name__)


@app.route('/set/<key>/<value>')
def set_val(key, value):
    result = r.set(key, value)
    return str(result)


@app.route('/get/<key>')
def get_val(key):
    result = r.get(key)
    return str(result)


app.run(host='localhost', port=8081)
