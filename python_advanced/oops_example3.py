class Book:
    def __init__(self):
        self.title=input("enter the name of the book:")
        self.author=input("enter the name of the author:")
        self.price=int(input("enter the price of the book:"))
        self.pages=int(input("enter the number of pages in the book:"))
        self.language=input("enter the languages of the book:")

    def gettitle(self):
        print("self.title")
    def getauthor(self):
        print(self.author)
    def getprice(self):
        print("self.price")

    def setauthor(self):
        self.author=input("enter the name of the author:")
    def settitle(self):
        self.title=input("enter the name of the book:")
    def setprice(self):
        self.price=int(input("enter the price of the book:"))

b=book()


