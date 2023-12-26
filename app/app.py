from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <p>Hello, everyone!</p>
        <p>My name is Muhammad Usman</p>
        <p>fa19-bcs-124</p>
        <button onclick="alert('name!')">Button 1</button>
        <button onclick="alert('id')">Button 2</button>
        <button onclick="alert('password')">Button 3</button>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
