from operations import add, sub, mult, div
from flask import Flask
from flask import request

app = Flask(__name__)



@app.get('/add')
def add():
    """"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = a + b

    html = f"<html><body><h1>{a} + {b} = {result}</h1></body></html>"
    return html