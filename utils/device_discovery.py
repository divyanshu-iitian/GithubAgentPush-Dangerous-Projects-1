from flask import Flask
from core.engine import Engine

app = Flask(__name__)
engine = Engine(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)