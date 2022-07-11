class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user(self):
        return self.username

    def get_pass(self):
        return self.password


class Manager(User):
    pass


class Member(User):
    memCount = 0

    def __init__(self, *inp):
        self.borrowC = 0
        self.borrowedBooks = []
        Member.memCount += 1
        if len(inp) == 2:
            super().__init__(inp[0], inp[1])
            self.memID = Member.memCount
        elif len(inp) == 4:
            super().__init__(inp[0], inp[1])
            self.memID = inp[2]
            self.borrowC = inp[3]

    def borrow_book(self, book):
        if self.borrowC < 5:
            self.borrowedBooks.append(book)
            self.borrowC += 1
        else:
            print("Too many borrowed books!")

    def return_book(self, book_id):
        if 0 >= book_id > 5:
            print("Please enter a valid number")
        elif self.borrowedBooks[book_id - 1] is not None:
            for i in range(book_id - 1, self.borrowC - 1):
                self.borrowedBooks[i] = self.borrowedBooks[i + 1]
            self.borrowedBooks.pop(self.borrowC - 1)
            self.borrowC -= 1
        else:
            print("Please enter a valid number")

    def get_borrowed_book(self, book_id):
        return self.borrowedBooks[book_id]

    def get_id(self):
        return self.memID

    def get_borrow_count(self):
        return self.borrowC
