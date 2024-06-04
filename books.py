class Book:
    def __init__(self, title: str, author: str, price: float, stock: int):
        self.title: str = title
        self.author: str = author
        self.price: float = price
        self.stock: int = stock

    def __str__(self):
        return f"Book details are, Title: {self.title}, author: {self.author}, price: {self.price} and," \
               f"stock available is: {self.stock}"

    def set_author(self, author: str):
        self.author: str = author

    def set_tile(self, title):
        self.title: str = title

    def set_price(self, price):
        self.price = price

    def set_stock(self, stock):
        self.stock = stock

    def get_author(self):
        return self.author

    def get_tile(self):
        return self.title

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def is_stock_available(self) -> bool:
        return self.stock > 0

    def increase_stock(self, quantity: int):
        self.stock += quantity

    def decrease_stock(self, quantity: int):
        self.stock -= quantity


books_available = []


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    price = 0
    stock = -1

    while price <= 0:
        try:
            price = int(input("Enter book price: "))
            if price < 0:
                price = int(input("Please Enter price greater than zero: "))
        except ValueError:
            price = int(input("Enter price of type integer: "))

    while stock < 0:
        try:
            stock = int(input("Enter book stock available: "))
            if stock < 0:
                stock = int(input("Please enter stock > 0: "))
        except ValueError:
            stock = int(input("Enter stock of type integer: "))

    book = Book(title, author, price, stock)
    books_available.append(book)
    print("Book added successfully!!!")
    return book


def calculate_book_price(title, quantity):
    for book in books_available:
        if book.title == title:
            return quantity * book.price

    print("book not found")
    return 0


def order_book(title, quantity):

    for book in books_available:
        if book.title == title:
            if quantity <= book.stock:
                print(f"Book placed successfully. Total price is: {calculate_book_price(title, quantity)}")
                return
            else:
                print(f"Stock not available. Available stock for order is: {book.stock}")
                return 

    print("Book not found")



add_book()
add_book()
order_book("billa", 30)
