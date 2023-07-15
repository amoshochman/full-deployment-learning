import configparser
import os

from flask import Flask, render_template, request
import redis

app = Flask(__name__, template_folder="templates")

config_file = 'config.ini'
config = configparser.ConfigParser()
config.read(config_file)

global_dict = {}

host = os.environ.get('REDIS_HOST') or config.get('Redis', 'host')
print("-----" + str(host))
if host and host != "test":
    pool = redis.ConnectionPool(host=host, port=6379, db=0)
    redis = redis.Redis(connection_pool=pool)
else:
    redis = None


@app.route("/")
def hello():
    return render_template('index.html')


def redis_str_to_int(string):
    return int(string.decode('utf-8'))


@app.route('/process', methods=['POST'])
def process():
    key = request.form.get('data')
    if key:
        value = redis.get(key) if redis else global_dict.get(key)
        if not value:
            if redis:
                redis.set(key, int(key) * 2)
            else:
                global_dict[key] = int(key) * 2

    local_dict = {}
    if redis:
        for key in redis.scan_iter():
            local_dict[redis_str_to_int(key)] = redis_str_to_int(redis[key])

    return " all values: " + str(local_dict if redis else global_dict)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
