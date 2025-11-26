class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def display_all_reviews(self):
        for review in self.reviews:
            print(review)

    def count_reviews(self):
        return len(self.reviews)

book = Book("My Hero Academia", "Kohei Horikoshi")
book.add_review("The story is so inspiring. I love it!")
book.display_all_reviews()
print(book.count_reviews())