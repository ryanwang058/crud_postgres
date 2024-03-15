import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from a .env file

conn = psycopg2.connect(
  database=os.environ.get("DB_NAME"),
  host=os.environ.get("DB_HOST"),
  user=os.environ.get("DB_USER"),
  password=os.environ.get("DB_PASSWORD"),
  port=os.environ.get("DB_PORT")
)

cursor = conn.cursor()
table = "students"

# read
cursor.execute(f"SELECT * FROM {table}")
rows = cursor.fetchall()
for row in rows:
  print(row)

cursor.close()
conn.close()
