import mysql.connector
import mysql

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password=""
      )
cursor = mydb.cursor()

try:
    cursor.execute("CREATE DATABASE if not exists mydatabase")
except:
    print("Failed to create Database!")
    exit()

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="mydatabase"
      )
cursor = mydb.cursor()

try:
    cursor.execute("CREATE TABLE if not exists registers (id INT AUTO_INCREMENT PRIMARY KEY, user VARCHAR(255), password VARCHAR(255), creation_time CHAR(19))")         
except:
    print("Failed to create Table!")
    exit()

cursor.close()
print("Successful SQL Database creation!")