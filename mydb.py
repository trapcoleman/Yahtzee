import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='data1234'
)

# cursor object
cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE yahtzee1")

