import os

from flask import Flask

app = Flask(__name__)


@app.get('/')
def index():
    env = os.environ.get("MY_ENV")
    return f"Hello worldzs {env} {__name__}"
