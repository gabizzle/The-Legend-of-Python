# 28 - DRY (Don't Repeat Yourself)
# Codédex

books = ['Atomic Habits',
         'Craft Coffee',
         'How to Taste Coffee',
         'A Little Life',
         'Ninth House']

books.append('The Compound Effect')
books.remove('Ninth House')
books.pop(1)

print(books)

def any(i):
    for books in i:
        if books:
            return True
        return False

print(any(books))