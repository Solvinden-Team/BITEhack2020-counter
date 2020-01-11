from flask import Flask


ppl = 0

app = Flask(__name__)


@app.route('/')
def index():
    with open("ppl.txt", "r") as f:
        return f.readline()


if __name__ == "__main__":
    app.run(port=8989, debug=False)
