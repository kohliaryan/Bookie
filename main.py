class Book:
    def __init__(self, title, author, genre, price, stock):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"{self.title} by {self.author} ({self.genre}) - ${self.price}")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, book):
        self.items.append(book)

    def remove_item(self, book):
        self.items.remove(book)

    def checkout(self):
        total = sum([book.price for book in self.items])
        self.items = []
        return total


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, book):
        self.shopping_cart.add_item(book)

    def remove_from_cart(self, book):
        self.shopping_cart.remove_item(book)

    def checkout(self):
        return self.shopping_cart.checkout()


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Order:
    def __init__(self, customer, books, total):
        self.customer = customer
        self.books = books
        self.total = total

    def display_info(self):
        print(f"Customer: {self.customer.name}")
        print("Books:")
        for book in self.books:
            book.display_info()
        print(f"Total: ${self.total}")