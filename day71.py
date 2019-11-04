# Python SQL 1
import mysql.connector

# connecting to our local database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd='14161995',
    database="mydatabase" #only works if mydatabase has been created
)

print(mydb)
# testing our connection
print(mydb.is_connected())

mycursor = mydb.cursor()

#creating database
#mycursor.execute("CREATE DATABASE mydatabase")

#checking available databases
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# create table
#mycursor.execute('CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))')

# check if table exists
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

# creating table with primary key
#mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# if database exists, this is how to create primary key on it
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")