from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Bonjour, monde !"

@app.route("/endpoint", methods=["POST"])
def endpoint():
    data = request.data
    eval(data)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
