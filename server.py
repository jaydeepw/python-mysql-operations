from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/login')
def login():
    return "You are now on LOGIN!"

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='scrypt')
        print(f'username {username} pass: {password} hash: {hashed_password}')

        # cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        # db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
