from flask import Flask, jsonify
from hello import greet

app = Flask(__name__)

@app.route('/greet/<name>')
def greet_route(name):
    return jsonify({"greeting": greet(name)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
