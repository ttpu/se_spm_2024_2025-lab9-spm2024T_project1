from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(testTablet)

def init_db():
    with sqlite3.connect('notes.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )''')

@app.route('/')
def index():
    with sqlite3.connect('notes.db') as conn:
        notes = conn.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect('notes.db') as conn:
            conn.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    with sqlite3.connect('notes.db') as conn:
        note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, note_id))
        return redirect(url_for('index'))
    return render_template('edit.html', note=note)

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    with sqlite3.connect('notes.db') as conn:
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
