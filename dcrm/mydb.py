import mysql.connector

dataBase=mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='rammech@2294'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE eldercos")

print("All Done!!!")