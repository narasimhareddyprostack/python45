import mysql.connector
dbcon = None
mycur = None
try:
    # create connect object
    dbcon = mysql.connector.connect(
        host='localhost', user='root', password='root', database='pro15')
    # print(dbcon)
    mycur = dbcon.cursor()
    # print(mycur)
    sql_st = '''
            insert into user(uid,uname,ucity,ucc)
            values(%s,%s,%s,%s)
             '''
    data = [(101, 'rahul', 'wayanad', 43434),
            (102, 'sonia', 'varanasi', 5839)
            ]
    mycur.executemany(sql_st, data)
    dbcon.commit()
    print("Data Inserted Successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    if mycur:
        mycur.close()
    if dbcon:
        dbcon.close()
