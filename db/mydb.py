import mysql.connector

# Connect to MySQL and select the database
con = mysql.connector.connect(
    host="localhost", user="root", password="1234", database="schooldb"
)
c = con.cursor()

# Insert data (phone numbers wrapped in quotes as VARCHAR/string)
# c.execute("""
#     INSERT INTO student (roll_no, name, age, place, phone, total_mark) VALUES
#     (101,'arun',20,'ekm','1234567890', 85),
#     (2,'Amal',21,'Los Angeles','9876543210', 90),
#     (3,'anu',19,'Chicago','5555555555', 75),
#     (4,'hari',22,'Houston','1111111111', 95),
#     (5,'manu',20,'Phoenix','2222222222', 80)
# """)

# con.commit()  # Save changes permanently in db
# print("Data inserted successfully")

# con.close()

# query="insert into student (roll_no, name, age, place, phone, total_mark) values (%s,%s,%s,%s,%s,%s)"

# data=(106,'kiran',12,'ekm','784151',140)

# c.execute(query,data)

# con.commit()

# print("Data inserted successfully")

# query="select * from student"
# c.execute(query)

# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)

# else:
#     print("No records found")

#read all attributes of a student with roll no=roll number entered by the user

# roll_no=int(input("enter the roll number:"))

# query="delete from student where roll_no=%s"
# data=(roll_no,)
# c.execute(query,data)
# con.commit()

roll_no=int(input("enter the roll number:"))
name=input("enter the name:")
age=int(input("enter the age:"))
place=input("enter the place:")
phone=input("enter the phone:")
total_mark=int(input("enter the total mark:"))

query="insert into student (roll_no, name, age, place, phone, total_mark) values (%s,%s,%s,%s,%s,%s)"

data=(roll_no,name,age,place,phone,total_mark)

c.execute(query,data)

con.commit()