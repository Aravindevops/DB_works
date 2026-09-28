import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.con=mysql.connector.connect(
            host="localhost",user="root",password="1234",database="automobile"
        )
        self.c=self.con.cursor()

    def list(self):
        query="select * from vehicle"
        self.c.execute(query)
        result=self.c.fetchall()
        if result:
            for row in result:
                print(row)
        else:
            print("no records found")


    def create(self):
        brand=input("enter the name of the brand:")
        model=input("enter model:")
        type=input("enter type:")
        price=int(input("enter price:"))
        year=int(input("enter year:"))
        query="insert into vehicle(brand,model,type,price,year) values (%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.c.execute(query,data)
        self.con.commit()
        print("inserted succesfully")

    def retrieve(self):
        id=int(input("Enter the vehicle id:"))
        query="select * from vehicle where id=%s"
        data=(id,)
        self.c.execute(query,data)
        result=self.c.fetchall()
        if result:
            for row in result:
                print(row)
        else:
            print("no record found")      

    def update(self):
        id=int(input("Enter the vehicle id:"))
        brand=input("enter the name of the brand:")
        model=input("enter model:")
        type=input("enter type:")
        price=int(input("enter price:"))
        year=int(input("enter year:"))
        query="update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data=(brand,model,type,price,year,id)
        self.c.execute(query,data)
        self.con.commit()
        print("updated succesfully")

    def delete(self):
        id=int(input("Enter the vehicle id:"))
        query="delete from vehicle where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c._rowcount>0:
            print("deleted succesfully")
        else:
            print("no record found")
        

vehicle_instance=VehicleListCreateRetrieveUpdateDelete()
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
        vehicle_instance.list()

    elif x==2:
        vehicle_instance.create()

    elif x==3:
        vehicle_instance.retrieve()

    elif x==4:
        vehicle_instance.update()

    elif x==5:
        vehicle_instance.delete()

    else:
        print("exit")
        break



    