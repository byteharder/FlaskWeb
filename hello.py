import os
from flask import Flask, url_for, request, render_template, redirect, flash, session

app = Flask(__name__)
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if 'username' not in session:
        if request.method == 'POST':
            if valid_login(request.form['username'], request.form['password']):
                flash("Successfully Logged In")
                session['username'] = request.form.get('username')
                return redirect(url_for('welcome'))
            else:
                error = 'Incorrect username and/or password'
        return render_template('login.html', error = error)
    return redirect(url_for('welcome'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', name=session['username'])
    return redirect(url_for('login'))

def valid_login(username, password):
    if str(username) == str(password):
        return True
    return False
 
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.secret_key = '\x19\xc12\x10\x01\x05\xba\xb4]&\xcf?\xfcv\x90\xffY\xc5Xk\xc9\x15Y\xa8'
    app.run(
        host=host,
        port=port,
        debug=True
    )