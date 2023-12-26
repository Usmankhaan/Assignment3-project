from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <html>
        <head>
            <style>
                body {
                    background-color: #f4f4f4;
                    font-family: Arial, sans-serif;
                }

                .container {
                    width: 50%;
                    margin: auto;
                    overflow: hidden;
                    padding: 20px;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    margin-top: 50px;
                }

                input[type="text"], input[type="password"] {
                    width: 100%;
                    padding: 8px 12px;
                    margin: 8px 0;
                    display: inline-block;
                    border: 1px solid #ccc;
                    box-sizing: border-box;
                    border-radius: 4px;
                }

                input[type="submit"] {
                    background-color: #4caf50;
                    color: white;
                    padding: 10px 15px;
                    margin: 8px 0;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }

                input[type="submit"]:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Signup Form</h2>
                <form>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required>

                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>

                    <input type="submit" value="Sign Up">
                </form>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
