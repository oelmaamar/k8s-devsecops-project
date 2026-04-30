from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps app running"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/config")
def config():
    app_mode = os.getenv("APP_MODE", "not-set")
    return {"app_mode": app_mode}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec
