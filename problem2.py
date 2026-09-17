# Problem 2: Special Methods

class BookPages:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"{self.pages} pages"

    def __add__(self, other):
        return BookPages(self.pages + other.pages)


# Create two BookPages objects
book1 = BookPages(120)
book2 = BookPages(85)

# Display the first object
print(book1)

# Add the two objects together
total_pages = book1 + book2

# Display the result
print(total_pages)
