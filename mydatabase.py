class conection:
  def __init__(self):

    import mysql.connector
    import mysql
    import pyodbc

    try:
      self.mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="mydatabase"
      )
    except:
      print("Failed to connect with MYSQL!")
      exit()
