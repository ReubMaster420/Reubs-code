class StockItem:
    def __init__(self, Title, DateAcquired, Onloan):
        self.Title = Title
        self.DateAcquired = DateAcquired
        self.Onloan = Onloan
    def ShowTitle(self):
        return self.Title
    def ShowDateAcquired(self):
        return self.DateAcquired
    def ShowOnLoan(self):
        return self.Onloan
    
class Book(StockItem):
    def __init__(self, Title, DateAcquired, Onloan, Author, isbn):
        super().__init__(Title, DateAcquired, Onloan)
        self.Author = Author
        self.isbn = isbn
    def ShowAuthor(self):
        return self.Author
    def ShowISBN(self):
        return self.isbn

#•	identifier NewBook 



NewBook = Book("Computers","12/11/2001", False,"A.Nyone", "099111")

print(NewBook.ShowTitle())
print(NewBook.ShowAuthor())
print(NewBook.ShowISBN())    
print(NewBook.ShowDateAcquired())    
print(NewBook.ShowOnLoan())