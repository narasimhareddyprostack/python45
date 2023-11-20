import mysql.connector
# provide credential to connect your database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="pro15")

mycursor = mydb.cursor()

sql_create = """create table employee(
eid int,
ename varchar(32),
esal float
)
 """
mycursor.execute(sql_create)
mydb.commit()
mycursor.close()
mydb.close()
