import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",user="root",password="1234"
# )

# c=con.cursor()

# c.execute("create database shop")

# con.close()

con = mysql.connector.connect(
    host="localhost",user="root",password="1234",database="shop"
)

c=con.cursor()

# query="create table product (product_id int primary key not null,name varchar(20) not null,brand varchar(20),category varchar(20),price int not null,stock int not null)"

# c.execute(query)
# con.commit()
# print("succesfully created")

def insert():
    p=int(input("enter the product id:"))
    name=input("enter the name:")
    brand=input("enter the brand:")
    category=input("enter the category:")
    price=int(input("enter the price:"))
    stock=int(input("enter the stock:"))

    query="insert into product (product_id,name,brand,category,price,stock)values(%s,%s,%s,%s,%s,%s)"
    data=(p,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
    print("successfully inserted")

def read():
    query="select * from product"
    c.execute(query)
    result=c.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("no records found")

def search():
    p=int(input("enter the product id:"))
    query="select * from product where product_id=%s"
    data=(p,)
    c.execute(query,data)
    result=c.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        print("no records found")
    con.commit()

def update():
    p=int(input("enter the product id:"))
    name=input("enter the name:")
    brand=input("enter the brand:")
    category=input("enter the category:")
    price=int(input("enter the price:"))
    stock=int(input("enter the stock:"))

    query="update product set name=%s,brand=%s,category=%s,price=%s,stock=%s where product_id=%s"
    data=(name,brand,category,price,stock,p)
    c.execute(query,data)
    con.commit()
    print("successfully updated")


def delete():
    p=int(input("enter the product id:"))
    query="delete from product where product_id=%s"
    data=(p,)
    c.execute(query,data)
    con.commit()
    print("successfully deleted")

while True:
    print("choice")
    print("1.insert product")
    print("2.read")
    print("3.search")
    print("4.update")
    print("5.delete")
    print("6.exit")

    x=int(input("enter your choice:"))

    if x==1:
        insert()
    elif x==2:
        read()
    elif x==3:
        search()
    elif x==4:
        update()
    elif x==5:
        delete()
    else:
        print(exit)
        break
c.close()
con.close()



    







