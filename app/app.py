from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Placeholder for user data (replace with a database in a real application)
users = {
    'user1': {'name': 'John Doe', 'registration_number': '12345'},
    'user2': {'name': 'Jane Doe', 'registration_number': '67890'}
}

@app.route('/')
def login_form():
    return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    registration_number = request.form['registration-number']

    # Check if the provided credentials match any user in the database
    for user, data in users.items():
        if data['name'] == username and data['registration_number'] == registration_number:
            # Redirect to the welcome page with the user's name
            return redirect(url_for('welcome', username=username))

    # If no match, redirect back to the login form
    return redirect(url_for('login_form'))

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
