from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python Flask in Kubernetes! version 3.0"

if __name__ == "__main__":
    # listen on all interfaces, port 5050
    app.run(host="0.0.0.0", port=5050)
