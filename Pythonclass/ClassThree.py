class Book():
    paper="white sheet"
    booksize=100*20*10

    def write(self):
        print("used to write the notes")
    def draw(self):
        print("used to draw the picture")

b=Book()
print(b.booksize)
print(b.paper)
b.draw()
b.write()
