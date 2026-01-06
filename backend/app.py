from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()
    return jsonify({"result": "Backend reached successfully!"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
