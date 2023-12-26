from flask import Flask

app = Flask(__name__)

@app.route('/')
def helo_world():
    return 'Hello, everyone!'
def heo_world():
    return ' My name is usman'
def ho_world():
    return 'I am stydent of BSCS'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
