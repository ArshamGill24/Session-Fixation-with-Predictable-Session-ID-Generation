from flask import Flask, render_template, request, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # In a real application, keep this secret

# Dictionary to simulate a user database
users = {
    'user1': 'password1',
    'user2': 'password2',
    'admin': 'admin',
    'root': 'root',
    'guest': 'guest',
    'test': 'test',
    'demo': 'demo',
    'user': 'user',
    'simple': 'simple'
}

# Counter to generate predictable session IDs
session_id_counter = 12345

# Function to generate predictable session IDs
def generate_predictable_session_id():
    global session_id_counter
    session_id = session_id_counter
    session_id_counter += 3
    return session_id

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]} with session ID {session["session_id"]}'
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user
        if username in users and users[username] == password:
            # Set a predictable session ID
            session_id = generate_predictable_session_id()
            session['username'] = username
            session['session_id'] = session_id
            resp = make_response(redirect(url_for('index')))
            resp.set_cookie('session_id', str(session_id))
            return resp

        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('session_id')
    return resp

@app.route('/fixate_session')
def fixate_session():
    username = request.args.get('username')
    session_id = request.args.get('session_id')
    if username and session_id:
        # Attacker sets a predictable session ID for a specific user
        session['username'] = username
        session['session_id'] = session_id
        resp = make_response(f'Session fixed with session_id {session_id} for user {username}. Now go to /login to use this session.')
        resp.set_cookie('session_id', session_id)
        return resp
    return 'No session_id or username provided'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
