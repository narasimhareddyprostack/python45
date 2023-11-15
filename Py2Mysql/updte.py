import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="root", database="pro15")
dbcursor = db.cursor()

sql_st = '''
        insert into employee values(103,'priyanka',55000.00)
        '''

dbcursor.execute(sql_st)
db.commit()

dbcursor.close()
db.close()
