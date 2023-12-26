from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <html>
        <head>
            <style>
                body {
                    background-color: #f0f0f0;
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }

                .container {
                    width: 400px;
                    padding: 30px;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
                }

                h2 {
                    text-align: center;
                    color: #333;
                }

                label {
                    display: block;
                    margin: 15px 0 5px;
                    color: #555;
                }

                input[type="text"], input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin: 8px 0;
                    display: inline-block;
                    border: 1px solid #ccc;
                    box-sizing: border-box;
                    border-radius: 5px;
                }

                input[type="submit"] {
                    background-color: #4caf50;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
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
