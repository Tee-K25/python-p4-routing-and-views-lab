#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:print>')
def print_string(print):
    # print("hello")
    return f'{print}'

@app.route('/count/<int:x>')
def count(x):
    result = ''
    for number in range(0,x+1):
        result += str(number) + "<br>"
    return result

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1,operation,num2):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
        # To handle division, we use a custom route segment 'div' instead of '/'
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2

        if result is not None:
            return f"The result of {num1} {operation} {num2} is: {result}"
        else:
            return "Invalid operation."

if __name__ == '__main__':
    app.run(port=5555, debug=True)
