"""
This script starts a Flask web application.

The web application listens on 0.0.0.0 and port 5000.

Routes:
- /: Displays "Hello HBNB!"
- /hbnb: Displays "HBNB"
- /c/<text>: Displays "C ", followed by the value of the text variable (replacing underscores with spaces)
- /python/<text>: Displays "Python ", followed by the value of the text variable (replacing underscores with spaces). The default value of text is "is cool"
- /number/<n>: Displays "n is a number" only if n is an integer
- /number_template/<n>: Displays an HTML page with "Number: n" inside an H1 tag if n is an integer

The script uses the option strict_slashes=False in route definitions.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"

@app.route('/c/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C ' followed by the value of the text variable (replacing underscores with spaces)."""
    return "C " + text.replace("_", " ")

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Displays 'Python ' followed by the value of the text variable (replacing underscores with spaces)."""
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a number' if n is an integer."""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page with 'Number: n' inside an H1 tag if n is an integer."""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
