from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Ericsson World! Please watch The Pursuit now 03052025 04:13PM :)"

if __name__ == "__main__":
    app.run(host='0.0.0.0')