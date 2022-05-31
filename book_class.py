class Book:
    def __init__(self, name, author, year_of_publish, publication, price):
        self.name = name
        self.author = author
        self.year_of_publish = year_of_publish
        self.publication = publication
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.author}, {self.year_of_publish}, {self.publication}, {self.price}'
