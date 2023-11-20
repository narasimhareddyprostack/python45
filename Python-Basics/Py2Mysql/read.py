import mysql.connector
# provide credential to connect your database
mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="pro15")

mycursor = mydb.cursor()

mycursor.execute('select * from employee')
empdata = mycursor.fetchall()
print(type(empdata))

for emp in empdata:
    print(emp)


mycursor.close()
mydb.close()
