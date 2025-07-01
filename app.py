from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello I am Shri, This application is created on Flask!"

@app.route('/home')
def hello():
    return "Python-App"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

