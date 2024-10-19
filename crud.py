import mysql.connector
try:
    con=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root@123",
    database="crud_op"
    )
    mycursor = con.cursor()
    print("Connection successfully established")
except:
    print("Connection failed")

#Creation of Database

mycursor.execute("CREATE DATABASE crud_op")
con.commit()
print("Database is successfully created")

#Creation of Table

mycursor.execute(
   """
    CREATE TABLE Registration(
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(50) NOT NULL,
    DATEOFBIRTH DATE NOT NULL)
""")
con.commit()
print("Table is created successfully")

#Inserting values into the table

mycursor.execute(
    """
    INSERT INTO Registration VALUES
    (1,"Anil","Anil88@gmail.com","2000-02-09"),
    (2,"Atul","Atul988@gmail.com","2001-12-09"),
    (3,"Amol","Amol998@gmail.com","2002-05-19")
""")
con.commit()
print("Data Inserted")

#Read Operation

mycursor.execute("Select * from Registration")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)

# Update Operation
mycursor.execute("update registration SET name='Amay' where id=2")
con.commit()
print("Updated successfully")

#Delete Operation

mycursor.execute("delete from registration where id=1")
con.commit()
print("Deleted successfully")