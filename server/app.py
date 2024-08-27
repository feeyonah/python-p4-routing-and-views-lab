#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


    

@app.route('/')
def index():
    print("Index route accessed")
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.errorhandler(404)
def page_not_found(e):
    print("404 error occurred")
    return "404 Error: Page not found", 404

# Route for printing a string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# Route for counting
@app.route('/count/<int:parameter>')
def count(parameter):
    return "\n".join(str(i) for i in range(parameter)) + "\n"

# Route for math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
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
    else:
        return "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
