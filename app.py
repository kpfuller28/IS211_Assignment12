from flask import Flask, g, render_template, redirect, request
import sqlite3
app = Flask(__name__)


@app.before_request
def before_request():
  g.db = sqlite3.connect("hw13.db")

@app.teardown_request
def teardown_request(exception):
  if hasattr(g, 'db'):
    g.db.close()


@app.route('/')
def main():
  print('landing page accessed')
  students = g.db.execute("SELECT * FROM students").fetchall()
  return render_template('index.html', students=students)

if __name__ == "__main__":
  app.run(debug=True)