from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

BASE_URL = 'https://api.icndb.com'


@app.route('/hello')
def hello_route():
    return jsonify({
        'hello': 'world'
    })


@app.route('/joke')
def get_random_joke():
    data = requests.get(BASE_URL + '/jokes/random').json()
    return jsonify(data)


@app.route('/jokes')
def all_routes():
    data = requests.get(BASE_URL + '/jokes').json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
