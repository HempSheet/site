#!C:\Users\MAKSIM\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi

print ("Content-type: text/html\n\n")

import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Rootpass12345',
    database='testdbSQL',
)

my_cursor = mydb.cursor()

#------make testdb in db-----
#my_cursor.execute("CREATE DATABASE testdbSQL")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)


#-----make tables-----
#my_cursor.execute("DROP TABLE IF EXISTS users")
#my_cursor.execute("CREATE TABLE users ("
#                  "id INTEGER, "
#                  "username VARCHAR(50), "
#                  "password VARCHAR(255), "
#                  "is_active BOOL, "
#                  "balance BIGINT, "
#                  "PRIMARY KEY (id))")

#my_cursor.execute("INSERT INTO users (id, username, password, is_active, balance)"
#                  "VALUES (1, 'Marly', '12345', '1', '2000')")


#my_cursor.execute("DROP TABLE IF EXISTS Session")
#my_cursor.execute("CREATE TABLE Session ("
#                  "id VARCHAR(10), "
#                  "user_id INTEGER(10), "
#                  "created_date TIME, "
#                  "expired_date TIME, "
#                  "data TEXT(200), "
#                  "ip VARCHAR(10), "
#                  "user_agent VARCHAR(150), "
#                  "PRIMARY KEY (id), "
#                  "FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)")

#my_cursor.execute("INSERT INTO Session (id, user_id, created_date, expired_date, data)"
#                  "VALUES (1, 1, '3:04:20', '3:10:20', 'today')")


my_cursor.execute("INSERT INTO transaction (id, created_date, type_transaction, amount, user_id)"
                  "VALUES (1, '3:04:20', 2, 1, 1)")
#my_cursor.execute("DROP TABLE IF EXISTS Transaction")
#my_cursor.execute("CREATE TABLE Transaction ("
#                  "id INTEGER(10), "
#                  "created_date TIME, "
#                  "type_transaction SMALLINT, "
#                  "amount BIGINT, "
#                  "user_id INTEGER(10), "
#                  "PRIMARY KEY (id), "
#                  "FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)")



#my_cursor.execute("SHOW TABLES")


#for table in my_cursor:
#    print(table[0])


#-----selects for db-----
my_cursor.execute("SELECT* FROM Transaction")
row = my_cursor.fetchone()

my_cursor.execute("SELECT* FROM users")
row1 = my_cursor.fetchone()

my_cursor.execute("SELECT* FROM Session")
row2 = my_cursor.fetchone()

#print(row)

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "not yet")
#x = "agdg" 
result_string = "" 
index = 0; 
for c in text1: 
    if(index%2 == 0): 
     result_string += c.lower() 
    else: 
     result_string += c.upper() 
    index+=1 

print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>RECOOL</title>
        </head>
        <link rel="stylesheet" href="index.css"> </head>
        <body>
        <div class="fff" id="container">
        <H1>PZ-prudko</H1>""")

print("<h1>Form data processing!</h1>")
print("<p>TEXT_1: {}</p>".format(result_string))
#print(result_string)
print("<h1>Data_Base</h1>")
print("<p>Users: {}</p>".format(row))
print("<p>Transaction: {}</p>".format(row1))
print("<p>Session: {}</p>".format(row2))

print("""
        <span class="labrat"></span>
        </div>

        <div class="foreground"></div>

        <div class="midground">
            <div class="tuna"></div>
        </div>

        <div class="background">
        </div>""")

print("""</body>
        </html>""")
