# http://flask.pocoo.org/docs/1.0/

# pip is a Python package manager (like a vast plugin library)
# we use pip to install Flask, and the line below is how we bring in Flask (and
# a variety of other functions and helpers) into our app
from flask import Flask, url_for, render_template, jsonify, request
app = Flask(__name__)

# INDEX PAGE
# the '/' is removed by default by the browser, but it represents the root page
# (eg www.facebook.com/)
@app.route("/")
def index():
    # When we visit http://localhost:5000 or http://127.0.0.1:5000 (they're the
    # same thing) we fire this function which returns a string which is displayed
    # in the browser
    return render_template('index.html')

# TEST ROUTES
# The below isn't necessary, it's just a way to test each route to make sure
# they do what you expect
with app.test_request_context():
    print(url_for('index'))

# What actually runs the app
app.run()
