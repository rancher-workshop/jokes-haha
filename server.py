from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/hello')
def hello_route():
    return jsonify({
        'hello': 'world'
    })


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
