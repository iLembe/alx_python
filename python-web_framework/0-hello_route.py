from flask import Flask

app = Flask(__name)

# Route definition with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__": # type: ignore
    app.run(host="0.0.0.0", port=5000)
