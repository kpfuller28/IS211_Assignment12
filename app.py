from flask import Flask, g, render_template, redirect, request, session
import sqlite3
app = Flask(__name__)

app.secret_key = 'bad test secret key'

@app.before_request
def before_request():
  g.db = sqlite3.connect("hw13.db")
  if not session.get('logged in') and request.path != '/login':
    return redirect('/login')

@app.teardown_request
def teardown_request(exception):
  if hasattr(g, 'db'):
    g.db.close()


@app.route('/')
def main():
  if session.get('logged in'):
    return redirect('/dashboard')
  else:
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] !='admin' or request.form['password'] != 'password':
      error = 'Invalid credentials. Please try again.'
    else:
      session['logged in'] = True
      return redirect('/dashboard')
  return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
  students = g.db.execute('SELECT * FROM students').fetchall()
  print(students)
  quizzes = g.db.execute('SELECT * FROM quizzes').fetchall()
  return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/student/add', methods=['GET', 'POST'])
def addStudent():
  if request.method == 'POST':
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    try:
      g.db.execute('INSERT INTO students VALUES (null, ?, ?)', (firstName, lastName))
      g.db.commit()
    except:
      error = 'An error occurred. Please try again, or navigate back to the dashboard.'
      return render_template('addStudent.html', error=error)
    return redirect('/dashboard')
  return render_template('addStudent.html')

@app.route('/quiz/add', methods=['GET', 'POST'])
def addQuiz():
  if request.method == 'POST':
    subject = request.form['subject']
    questions = request.form['questions']
    day = request.form['day']
    month = request.form['month']
    year = request.form['year']
    date = f"{year}-{month}-{day}"
    try:
      g.db.execute('INSERT INTO quizzes VALUES (null, ?, ?, ?)', (subject, questions, date) )
      g.db.commit()
    except:
      error = 'There was an error. Please make sure all information is correct and try again.'
      return render_template('/addQuiz', error=error)
    return redirect('/dashboard')
  return render_template('/addQuiz.html')
if __name__ == "__main__":
  app.run(debug=True)