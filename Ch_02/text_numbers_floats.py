
# incremental source code for the lesson "numbers and floats"
# section 2: lecture 10


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


@app.route('/new/')
def query_string(greeting='hello'):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {0} </h1>'.format(query_val)


@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='mina'):
    return '<h1> hello there ! {} </>'.format(name)


# strings
@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> here is a string: ' + name + '</h1>'


# numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> the number you picked is: ' + str(num) + '</h1>'


# add numbers
@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'


# floats
@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1, num2):
    return '<h1> the product is : {}'.format(num1 * num2) + '</h1>'