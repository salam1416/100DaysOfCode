import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd='14161995',
    database="mydatabase" #only works if mydatabase has been created
)

mycursor = mydb.cursor()

# ordering the database
sql = "SELECT * FROM customers ORDER BY id DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# deleting a record from the database
sql = "DELETE FROM customers WHERE address = 'Highway 21'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "records deleted")

# you can also drop a table with 
#sql = "DROP TABLE customers"
# drop if exists
#sql = "DROP TABLE IF EXISTS customers"
