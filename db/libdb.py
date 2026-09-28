import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",user="root",password="1234",database="library_db"
        )
        self.c=self.con.cursor()

    def list(self):
        query="select * from book"
        self.c.execute(query)
        result=self.c.fetchall()
        if result:
            for row in result:
                print(row)
        else:
            print("no records found")


    def create(self):
        title=input("enter the name of the book:")
        author=input("enter the name of the author:")
        price=int(input("enter the price of the book:"))
        pages=int(input("enter the number of pages in the book:"))
        language=input("enter the language of the book:")
        query="insert into book(title,author,price,pages,language) values (%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.c.execute(query,data)
        self.con.commit()
        print("inserted succesfully")

    def retrieve(self):
        id=int(input("Enter the book_id:"))
        query="select * from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        result=self.c.fetchall()
        if result:
            for row in result:
                print(row)
        else:
            print("no record found")      

    def update(self):
        id=int(input("Enter the book_id:"))
        title=input("enter the updated name of the book:")
        author=input("enter the updated name of the author:")
        price=int(input("enter the updated price of the book:"))
        pages=int(input("enter the updated number of pages in the book:"))
        language=input("enter the updated language of the book:")
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.c.execute(query,data)
        self.con.commit()
        print("updated succesfully")

    def delete(self):
        id=int(input("Enter the book_id:"))
        query="delete from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c._rowcount>0:
            print("deleted succesfully")
        else:
            print("no record found")
        


book_instance=BookListCreateRetrieveUpdateDelete()
while True:
    print("enter your choice:")
    print("1.list")
    print("2.create")
    print("3.retrieve")
    print("4.update")
    print("5.delete")
    print("6.exit")

    x=int(input("enter your choice:"))
    if x==1:
        book_instance.list()

    elif x==2:
        book_instance.create()

    elif x==3:
        book_instance.retrieve()

    elif x==4:
        book_instance.update()

    elif x==5:
        book_instance.delete()

    else:
        print("exit")
        break



    