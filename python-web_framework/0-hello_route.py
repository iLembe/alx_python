"""
This is a simple Flask web application that displays 'Hello HBNB!' on the root URL.
"""

from flask import Flask

app = Flask(__name)

# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when the root URL is accessed."""
    return "Hello HBNB!"

if __name__ == "__main__": # type: ignore
    app.run(host="0.0.0.0", port=5000)
