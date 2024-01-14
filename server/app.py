#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param:str):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param:int):
    result = ''
    for number in range(0,param+1):
        result += str(number) + "<br>"
    return result

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1:int,operation:str,num2:int):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2

        if result is not None:
            return str(result)
        else:
            return "Invalid operation."

if __name__ == '__main__':
    app.run(port=5555, debug=True)
