from flask import Flask, render_template, request
import redis

app = Flask(__name__, template_folder="templates")
my_dict = {}


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    if data not in my_dict:
        my_dict[data] = int(data) * 2
    return str(str(my_dict) + value.decode('utf-8'))


if __name__ == '__main__':
    pool = redis.ConnectionPool(host='redis', port=6379, db=0)
    redis = redis.Redis(connection_pool=pool)
    redis.set('mykey', 'Hello from Python!')
    value = redis.get('mykey')

    app.run(debug=True, host="0.0.0.0")