CREATE TABLE Teachers (
   id integer PRIMARY KEY AUTOINCREMENT,
   name varchar,
   birthday datetime
);

CREATE TABLE Subjects (
   id integer PRIMARY KEY AUTOINCREMENT,
   name varchar
);

CREATE TABLE Faculties (
   id integer PRIMARY KEY AUTOINCREMENT,
   name varchar
);

CREATE TABLE Groups (
   id integer PRIMARY KEY AUTOINCREMENT,
   name varchar,
   faculty_id integer,
   FOREIGN KEY (faculty_id) REFERENCES Faculties(id)

);

CREATE TABLE Students (
   id integer PRIMARY KEY AUTOINCREMENT,
   name varchar,
   age integer,
   group_id integer,
   FOREIGN KEY (group_id) REFERENCES Groups(id)
);

CREATE TABLE Exams (
   id integer PRIMARY KEY AUTOINCREMENT,
   date datetime,
   subject_id integer,
   group_id integer,
   teacher_id integer,
   FOREIGN KEY (subject_id) REFERENCES Subjects(id),
   FOREIGN KEY (group_id) REFERENCES Groups(id),
   FOREIGN KEY (teacher_id) REFERENCES Teachers(id)

);

CREATE TABLE Mark (
   id integer PRIMARY KEY AUTOINCREMENT,
   value integer,
   student_id integer,
   exam_id integer,
   FOREIGN KEY (student_id) REFERENCES Students(id),
   FOREIGN KEY (exam_id) REFERENCES Exams(id)

);



