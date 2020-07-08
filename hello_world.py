#!/usr/bin/python
from flask import Flask

PORT = 9090
MESSAGE = ''' TEST 1<br/>Alhamdulillah.  All Praise is due to Allah <br/>Hello, world, and I call you to Islam!\n'''

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=PORT)
