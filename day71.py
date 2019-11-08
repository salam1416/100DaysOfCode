# Python SQL server 2
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd='14161995',
    database="mydatabase" #only works if mydatabase has been created
)

mycursor = mydb.cursor()

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("John", "Highway 21")
# inserting many records
'''
val = [
    ('Peter', 'Lowstreet 4'),
    ('Any', 'Apple st 652'),
    ('Hanna', 'Mountain 21')
]
'''
#val = ("Michelle", "Blue Village")
#mycursor.execute(sql, val)
#mycursor.executemany(sql, val)

#mycursor.execute("SELECT * FROM customers")
#sql = "SELECT * FROM customers WHERE address = 'Lowstreet 4'"
sql = "SELECT * FROM customers WHERE address Like '%age%' "
mycursor.execute(sql)
#mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
#myresult = mycursor.fetchone()

for x in myresult:
    print(x)

#print(myresult)

#mydb.commit()

#print(mycursor.rowcount, "records were inserted.")
#print(mycursor.lastrowid())