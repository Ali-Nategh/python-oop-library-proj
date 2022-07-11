from users import Manager, Member
from inscription import Book, Journal


class Library:
    members = []
    managers = []
    books_list = []
    journals_list = []

    current_member = 0
    counter_m = 0
    counter_b = 0
    counter_j = 0

    @classmethod
    def print_line(cls):
        print("----------")

    @classmethod
    def mem_auth(cls, m_user, m_pass):
        for i in range(len(Library.members)):
            if Library.members[i] is not None:
                if m_user == Library.members[i].get_user() and m_pass == Library.members[i].get_pass():
                    Library.current_member = Library.members[i].get_id() - 1
                    return True
        return False

    @classmethod
    def set_current_member(cls, m_id):
        Library.current_member = m_id

    @classmethod
    def man_auth(cls, m_user, m_pass):
        for i in range(len(Library.managers)):
            if Library.managers[i] is not None:
                if m_user == Library.managers[i].get_user() and m_pass == Library.managers[i].get_pass():
                    return True
        return False

    @classmethod
    def set_manager(cls, username, password):
        m = Manager(username, password)
        Library.managers.append(m)

    @classmethod
    def add_member(cls, username, password):
        m = Member(username, password)
        Library.members.append(m)
        Library.counter_m += 1

    @classmethod
    def add_member2(cls, m_user, m_pass, m_id, borrow_c):
        m = Member(m_user, m_pass, m_id, borrow_c)
        Library.members.append(m)
        Library.counter_m += 1

    @classmethod
    def add_book(cls, name, writer, category, b_id, stock):
        b = Book(name, writer, category, b_id, stock)
        Library.books_list.append(b)
        Library.counter_b += 1

    @classmethod
    def add_journal(cls, name, j_num, date, category, j_id, stock):
        j = Journal(name, j_num, date, category, j_id, stock)
        Library.journals_list.append(j)
        Library.counter_j += 1

    @classmethod
    def show_all(cls):
        print("Books:")
        for i in range(len(Library.books_list)):
            b = Library.books_list[i]
            if b is None:
                break
            print(f"name: {b.get_name()} - id: {b.get_id()}")
        print("Journals:")
        for i in range(len(Library.journals_list)):
            j = Library.journals_list[i]
            if j is None:
                break
            print(f"name: {j.get_name()} - id: {j.get_id()}")

    @classmethod
    def book_not_found(cls):
        print("No books with that ID \n Try again")
        Library.print_line()

    @classmethod
    def lib_borrow_book(cls, b_id):
        if b_id <= 0 or b_id > 5:
            print("Please enter a valid number\n")
        for i in range(len(Library.books_list)):
            try:
                b = Library.books_list[i]
                if b_id == b.get_id():
                    m = Library.members[Library.current_member]
                    m.borrow_book(b)
                    break
                elif i == len(Library.books_list):
                    Library.book_not_found()
            except Exception as e:
                Library.book_not_found()
                break

    @classmethod
    def borrowed(cls):
        for i in range(5):
            try:
                mem = Library.members[Library.current_member]
                if mem.get_borrowed_book(i) is not None:
                    print(f"{i + 1} {mem.get_borrowed_book(i).get_name()}")
                else:
                    break
            except Exception as e:
                break

    @classmethod
    def lib_return_book(cls, b_id):
        try:
            Library.members[Library.current_member].return_book(b_id)
        except Exception:
            print("Wrong number or empty")

    @classmethod
    def remove_book(cls, b_id):
        continue_loop = True
        for i in range(len(Library.books_list)):
            flag = True
            if not continue_loop:
                break
            try:
                for j in range(len(Library.members)):
                    try:
                        mem = Library.members[j]
                        if mem is None:
                            break
                        for k in range(5):
                            if mem.get_borrowed_book(k) is None:
                                break
                            if mem.get_borrowed_book(k).get_id() == b_id:
                                print(f"This book is borrowed by {mem.get_user()} you can't delete it")
                                flag = False
                                continue_loop = False
                                break
                    except IndexError:
                        break
                b = Library.books_list[i]
                if b.get_id() == b_id and flag:
                    Library.books_list.remove(b)
                    break
            except Exception:
                print("Error")
                break

    @classmethod
    def write_data(cls):
        pass

    @classmethod
    def read_data(cls):
        pass
