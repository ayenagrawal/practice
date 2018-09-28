import mysql.connector as mysqlobj
mydb = mysqlobj.connect(user='root', password='Password', host='localhost', auth_plugin='mysql_native_password', database="mydatabase")
mycursor = mydb.cursor()

# creating a database
#mycursor.execute("create database mydatabase")

# checking databases
'''mycursor.execute("show databases")
for x in mycursor:
    print(x)'''

# create table
#mycursor.execute("create table customers (name varchar(255), address varchar(255))")

# view present databases
'''mycursor.execute("show tables")
for x in mycursor:
    print(x)'''

# create a table with a primary key
# mycursor.execute("CREATE TABLE customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# alter table structure
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# insert data into a table
#mycursor.execute("INSERT INTO customers1 (name, address, id) VALUES (%s, %s, %s)", ("Abcde Pqrst", "Hyderabad", 105))
# mydb.commit()

# insert multiple values at a time into a table
'''val = [
    (101, "Amit", "Varanasi"),
    (102, "Rajesh", "Bhopal"),
    (103, "Ram", "Patna"),
    (104, "Krishna", "Dwarka")
]
mycursor.executemany("insert into customers1 values(%s,%s,%s)", val)
mydb.commit()
print(mycursor.rowcount, "was inserted")'''

# fetching data by some condition
# mycursor.execute("select * from customers1 where address='Varanasi'")

# fetching data with using order by clause
# mycursor.execute("select * from customers1 order by Name desc")

# deleteing a row
'''mycursor.execute("delete from customers1 where address='Hyderabad'")
mydb.commit()
print(mycursor.rowcount)'''

# renaming a table
# mycursor.execute("alter table customers1 rename customers")

# fetching all rows from a table
mycursor.execute("select * from customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# fetching a single row from a table
'''mycursor.execute("select * from customers1")
myresult = mycursor.fetchone()
print(myresult)'''

# drop a table
# mycursor.execute("drop table customers") or "drop table if exixts customers"
