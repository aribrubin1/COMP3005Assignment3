import psycopg2
class database:

    def __init__(self):
        self.conn = psycopg2.connect(database="Assignment3",
                        host="localhost",
                        user="postgres",
                        password="student")
        self.cur = self.conn.cursor()

    def getAllStudents(self):
        self.cur.execute("SELECT * FROM students")
        all = self.cur.fetchall()
        for i in all:
            print(i)

    # adding students
    def addStudent(self,first_name, last_name, email, enrollment_date):
        try:
            self.cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                        (first_name, last_name, email, enrollment_date))
            self.conn.commit()
        except Exception as e:
            print("Could not add:", e)

    # updating student emails
    def updateStudentEmail(self,student_id, new_email):
        try:
            self.cur.execute("UPDATE students SET email = '" + new_email + "' WHERE student_id = " + student_id + ";")
            self.conn.commit()
        except Exception as e:
            print("Could not edit:", e)

    # deleting student
    def deleteStudent(self,student_id):
        try:
            self.cur.execute("DELETE FROM students WHERE student_id = " + student_id + ";")
            self.conn.commit()
        except Exception as e:
            print("Could not delete:", e)
