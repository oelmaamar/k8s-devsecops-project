from flask import Flask
import os
import logging
import sys

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

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec
