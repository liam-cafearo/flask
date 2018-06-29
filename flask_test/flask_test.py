# We import the Flask class. We know that it’s a class because
# the convention in Python is to start classes with a capital letter.
from flask import Flask

# We create an instance of our class and pass it the name of our
# module. Our app instance needs to know the name so it can find
# our templates and static folders and files.
app = Flask(__name__)

# A route has been defined using a decorator.
# The decorator is saying ‘if the user navigates to the address /,
# then run the function below’, i.e. the decorated function.


@app.route('/')
# Our function returns the text ‘Hello World’ –
# this is what the user will see in their browser.
def hello_world():
    return 'Hello World!'


# We run our app using app.run(), unsurprisingly.
# We use if __name__ == ‘__main__’: to ensure the app is only run
# when instantiated directly from the Python interpreter, not when
# imported from another file.
if __name__ == '__main__':
    app.run(debug=True)
