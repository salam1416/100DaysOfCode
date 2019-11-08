# My Employee database
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "14161995",
    database = "MyEmployee"
)

mycursor = mydb.cursor()

# to create the database, then I'll access it from the above connection
#mycursor.execute("CREATE DATABASE MyEmployee")

# to create the table, only needed with the first run
#mycursor.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255), LastName VARCHAR(255), Age int, Gender VARCHAR(6), Salary float)")

# the below block to add the table
'''
sql = "INSERT INTO Employee (FirstName, LastName, Age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('Ahmed', 'Ali', 30, 'Male', 10000.0),
    ('Khalid', 'Mohammed', 34, 'Male', 7000.0),
    ('Norah', 'Saleh', 29, 'Female', 7000.0)
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record were inserted")
'''

print('# Q1')
mycursor.execute("SELECT * FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('# Q2')
mycursor.execute('SELECT FirstName, Gender, Salary FROM Employee')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('# Q3')
mycursor.execute("SELECT * FROM Employee ORDER BY FirstName DESC")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('# Q4, deleting record with Age = 34')
mycursor.execute("DELETE FROM Employee WHERE Age = 34")
mydb.commit()
mycursor.execute("SELECT * FROM Employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
