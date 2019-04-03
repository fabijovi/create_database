import mysql.connector

mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= 'password'
)

cursor = mydb.cursor()
newdb = 'testdb'
sql = ("""SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = (%s)""")

cursor = mydb.cursor()
cursor.execute(sql, (newdb,))
myresult = cursor.fetchone()
print (myresult)

if myresult == None:
    print("DATABASE DOES NOT EXIST, CREATING DATABASE...")
    sql = ("CREATE DATABASE (%s)")
    cursor.execute(sql, (newdb,))
    mydb.commit()
    print(".............................................")
    print("DATABASE SUCCESSFULLY CREATED")

else:
    for i in myresult:
        if i == newdb:
            print("DATABASE ALREADY EXISTS")

        else:
            pass
