from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/explain", methods=["POST"])
def explain():
    print("✅ /explain route HIT")
    data = request.get_json()
    return jsonify({"result": "Backend is connected successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
