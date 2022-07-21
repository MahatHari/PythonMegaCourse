from re import template
from flask import Flask, render_template

# create flask instance
app = Flask(__name__)

# create routes


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
