from flask import flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "hello world deployed using argo cd"

if __name__ == "__main__":
    app.run(host='0.0.0.0')