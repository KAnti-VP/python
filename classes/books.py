class Book:
    def __init__(self, writer, title, edition, year):
        self.writer = writer
        self.title = title
        self.edition = edition
        self.year = year
    
    def __str__(self):
        return f'Book(writer: {self.writer}, title: {self.title}, edition: {self.edition}, year: {self.year})'

print('1-2. feladat')
books = []
with open('books.txt', 'r') as f:
    writer, title, edition, year = 0, 1, 2, 3
    f.readline()
    for row in f:
        data = row.strip().split('\t')
        # book = Book(data[0], data[1], data[2], data[3])
        book = Book(data[writer], data[title], data[edition], int(data[year]))
        books.append(book)

print('3. feladat')
for book in books:
    print(book)

print('4. feladat')
oldest = books[0]
for book in books:
    if book.year < oldest.year:
        oldest = book
print(oldest)

print('5. feladat')
for book in books:
    if book.year > 1900 and book.year <= 2000:
        print(book)

print('6. feladat')
book = '\n-\tThe Book\t1st\t2024'
with open('books.txt', 'a') as f:
    f.write(book)
