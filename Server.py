from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def get_hello():
    return jsonify("hola dios soy yo de nuevo ")


if __name__ == "__main__":
    app.run("localhost", port=3000)
