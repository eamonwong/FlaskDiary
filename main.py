from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# List to store diary entries
diary_entries = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry = request.form['entry']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        diary_entries = session.get('diary_entries', [])
        diary_entries.append((entry, timestamp))
        session['diary_entries'] = diary_entries
        return redirect('/')

    diary_entries = session.get('diary_entries', [])
    return render_template('index.html', diary_entries=diary_entries)


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_entry(index):
    if request.method == 'POST':
        new_entry = request.form['entry']
        diary_entries = session.get('diary_entries', [])
        if index >= 0 and index < len(diary_entries):
            diary_entries[index] = (new_entry, diary_entries[index][1])
            session['diary_entries'] = diary_entries
        return redirect('/')

    diary_entries = session.get('diary_entries', [])
    if index >= 0 and index < len(diary_entries):
        return render_template('edit.html', index=index, entry=diary_entries[index][0])
    return redirect('/')


@app.route('/delete/<int:index>', methods=['GET'])
def delete_entry(index):
    diary_entries = session.get('diary_entries', [])
    if index >= 0 and index < len(diary_entries):
        del diary_entries[index]
        session['diary_entries'] = diary_entries
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)