import psycopg2
from dotenv import load_dotenv
import os

class CRUD:
  def __init__(self, table):
    load_dotenv() # Load environment variables from a .env file
    self.conn = psycopg2.connect(
      database=os.environ.get("DB_NAME"),
      host=os.environ.get("DB_HOST"),
      user=os.environ.get("DB_USER"),
      password=os.environ.get("DB_PASSWORD"),
      port=os.environ.get("DB_PORT")
    )
    self.table = table # Name of the table to do CRUD operations

  def __del__(self):
    self.conn.close()

  def getAllStudents(self):
    """
    READ operation: Get all students from the tables
    """
    with self.conn.cursor() as cursor:
      cursor.execute(f"SELECT * FROM {self.table}")
      rows = cursor.fetchall()
      for row in rows:
        print(row)
  
  def addStudent(self, first_name, last_name, email, enrollment_date):
    """
    CREATE operation: Add a new student to the table

    @param first_name: string, First name of the student
    @param last_name: string, Last name of the student
    @param email: string, Email which includes the @ symbol
    @param enrollment_date: string, Date when the student enrolled in the format YYYY-MM-DD
    """
    query = f"INSERT INTO {self.table} (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
    with self.conn.cursor() as cursor:
      cursor.execute(query, (first_name, last_name, email, enrollment_date))
      self.conn.commit()

  def updateStudentEmail(self, student_id, new_email):
    """
    UPDATE operation: Update the email of a student

    @param student_id: int, ID of the student
    @param new_email: string, New email of the student
    """
    query = f"UPDATE {self.table} SET email = %s WHERE student_id = %s"
    with self.conn.cursor() as cursor:
      cursor.execute(query, (new_email, student_id))
      self.conn.commit()

  def deleteStudent(self, student_id):
    """
    DELETE operation: Delete a student from the table

    @param student_id: int, ID of the student
    """
    query = f"DELETE from {self.table} WHERE student_id = %s"
    with self.conn.cursor() as cursor:
      cursor.execute(query, (student_id,))
      self.conn.commit()