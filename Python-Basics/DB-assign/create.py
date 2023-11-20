import mysql.connector
dbcon = None
mycur = None
try:
    # create connect object
    dbcon = mysql.connector.connect(
        host='localhost', user='root', password='root', database='pro15')
    print(dbcon)
    mycur = dbcon.cursor()
    print(mycur)
    sql_st = '''
            create table USER(
                uid int,
                uname varchar(32),
                ucity varchar(32)
            ) 
           '''
    mycur.execute(sql_st)
    dbcon.commit()
    print("Table Created Successfully")

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    if mycur:
        mycur.close()
    if dbcon:
        dbcon.close()
