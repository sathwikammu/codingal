class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.borrowed=False
    def borrow(self):
        self.borrowed=True
        print(self.title,"he borrowed successfully")

    def return_book(self):
        self.borrowed=False
        print(self.title,"he has returned the book")

book1=book("python basics","sathwik")
book2=book("java","jhon")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()


