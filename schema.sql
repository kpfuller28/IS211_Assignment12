CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
)

CREATE TABLE quizzes (
  id INTEGER PRIMARY KEY,
  quiz_subject TEXT,
  num_questions INTEGER,
  date_given DATE
)
CREATE TABLE results (
  student_id INTEGER,
  quiz_id INTEGER,
  score INTEGER NOT NULL,
  FOREIGN KEY(student_id) REFERENCES students(id)
  FOREIGN KEY(quiz_id) REFERENCES quiz(id)
  PRIMARY KEY(student_id, quiz_id)
)