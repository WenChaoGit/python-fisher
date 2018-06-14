from flask import Flask, make_response
from config import DEBUG

__author__ = '文朝'
app = Flask(__name__)


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain'
    }
    return '<html/>', 301, headers


if __name__ == '__main__':
    app.run(debug=DEBUG)
