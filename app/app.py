from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sample Web App</title>
            <style>
                body {
                    text-align: center;
                    font-family: Arial, sans-serif;
                }
                header {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px;
                }
                footer {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px;
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Sample Web App</h1>
            </header>
            
            <p>Hello! I am Usman from BCS8.</p>
            
            <footer>
                &copy; 2023 Sample Web App
            </footer>
        </body>
        </html>
    '''

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0')
