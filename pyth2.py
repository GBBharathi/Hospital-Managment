import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="4587"
)

print(mydb)
