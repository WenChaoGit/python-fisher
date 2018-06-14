
from flask import Flask
from config import DEBUG

__author__ = '文朝'
app = Flask(__name__)

@app.route('/hello')
def hello():
   return 'hello,world'

app.run(debug=DEBUG)
