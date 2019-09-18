class Book:
    def __init__(self, title="Software Engineering SJU", isbn=""):
        self.title = title
        self.isbn = isbn
    
    def printBook(self):
        print(self.title + ", " + self.isbn)