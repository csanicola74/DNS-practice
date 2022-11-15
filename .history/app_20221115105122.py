
from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World, it is Caroline'


@app.route('/predict_api', methods=["GET", "POST"])
def list_post():
    json_body = request.get_json()
    predictions = 2 * json_body[0]
    predictions = list(predictions)
    return jsonify(results=predictions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
