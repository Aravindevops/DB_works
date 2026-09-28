class Category:
    def __init__(self):
        self.category_name=input("Enter category name:")

    def show_category(self):
        print("Category: ",self.category_name)


class product(Category):
    def __init__(self):
        super().__init__()
        self.product_name=input("Enter product name:")
        self.price=int(input("Enter product price:"))
        self.quantity=int(input("Enter product quantity:"))

    def total_price(self):
        print("Total price:",self.price*self.quantity)


c=product()
c.total_price()

