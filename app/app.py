from flask import Flask

app = Flask(__name__)

@app.route('/')
def helo_world():
    return 'Hello, everyone!\nMy name is Muhammad Usman\nI am student of BSCS'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
