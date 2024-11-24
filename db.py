import sqlite3


def main():
  connection = sqlite3.connect("hw13.db")
  cursor = connection.cursor()
  print('running app.py')
  cursor.execute("INSERT INTO students VALUES (null, 'John','Smith')")
  cursor.execute("INSERT INTO quizzes VALUES (null, 'Python Basics', 5, '2015-02-05')")
  cursor.execute("INSERT INTO results VALUES (1, 1, 85)")
  connection.commit()
  students = cursor.execute("SELECT * FROM students")
  print(students.fetchall())
  quizzes = cursor.execute("SELECT * FROM quizzes")
  print(quizzes.fetchall())
  results = cursor.execute("SELECT * FROM results")
  print(results.fetchall())
  connection.close()

main()