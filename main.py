from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    #return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
    return 'Pagina de Joel'


if __name__ == '__main__':
    app.run(debug=True, port=80)
