# Python SQL 3
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd='14161995',
    database="mydatabase" #only works if mydatabase has been created
)

mycursor = mydb.cursor()
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'East Mich' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record affected")

# There's the OFFSET and LIMIT methods that we should know about
#Joins statements
# I will not write the examples here; I will somehow do it in the next two lessons