from flask import Flask, render_template, request, redirect, session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dictionary to store user accounts
users = {
    # create own username here 
    'username': {
        # create password in () 
        'password': generate_password_hash('password'),
        'diary_entries': []
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    diary_entries = users[user_id].get('diary_entries', [])

    if request.method == 'POST':
        entry = request.form['entry']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        diary_entries.append((entry, timestamp))
        users[user_id]['diary_entries'] = diary_entries
        return redirect('/')

    return render_template('index.html', diary_entries=diary_entries)

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_entry(index):
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    diary_entries = users[user_id].get('diary_entries', [])

    if request.method == 'POST':
        new_entry = request.form['entry']
        if index >= 0 and index < len(diary_entries):
            diary_entries[index] = (new_entry, diary_entries[index][1])
            users[user_id]['diary_entries'] = diary_entries
        return redirect('/')

    if index >= 0 and index < len(diary_entries):
        return render_template('edit.html', index=index, entry=diary_entries[index][0])
    return redirect('/')

@app.route('/delete/<int:index>', methods=['GET'])
def delete_entry(index):
    if 'user_id' not in session:
        return redirect('/login')

    user_id = session['user_id']
    diary_entries = users[user_id].get('diary_entries', [])

    if index >= 0 and index < len(diary_entries):
        del diary_entries[index]
        users[user_id]['diary_entries'] = diary_entries
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return 'Username already exists'

        hashed_password = generate_password_hash(password)
        users[username] = {'password': hashed_password, 'diary_entries': []}
        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users or not check_password_hash(users[username]['password'], password):
            return 'Invalid username or password'

        session['user_id'] = username
        return redirect('/')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
