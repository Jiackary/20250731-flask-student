import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(port=port, host="0.0.0.0")