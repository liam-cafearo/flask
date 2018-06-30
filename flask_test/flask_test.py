# We import the Flask class. We know that it's a class because
# the convention in Python is to start classes with a capital letter.
from flask import Flask, abort
from flask import render_template

# We create an instance of our class and pass it the name of our
# module. Our app instance needs to know the name so it can find
# our templates and static folders and files.
app = Flask(__name__)

# add age dictionary (normally stored in a database)
ages = {
    'bob': '43',
    'alice': '29'
}

# add route that displays information about a user

# You can see we've used <user> as a placeholder in the url.
# This means that the function user_profiles will receive this
# part of the url as the user argument.

# `user` and `age` are both local variables. 
# `user` is the parameter passed to the `users` function 
# (which is read off the URL), while `age` is set on line 28.
@app.route('/users/<user>')
def users(user):
    age = ages.get(user)
    # Instead of returning a string, we call render_template with 
    # the name of the template, and the variable we want to be 
    # rendered.
    return render_template('user.html', user=user, age=age)

    # if age:
    #     return '%s is %s years old' % (user, age)
    # else:
    #     abort(404)

# A route has been defined using a decorator.
# The decorator is saying 'if the user navigates to the address /,
# then run the function below', i.e. the decorated function.


@app.route('/')
# Our function returns the text 'Hello World' -
# this is what the user will see in their browser.
def hello_world():
    return 'Hello World!'
    # Introduce an Error (produces ZeroDivision Error)
    # a, b = 1, 0
    # return a / b


# We run our app using app.run(), unsurprisingly.
# We use if __name__ == '__main__': to ensure the app is only run
# when instantiated directly from the Python interpreter, not when
# imported from another file.
if __name__ == '__main__':
    app.run(debug=True)

