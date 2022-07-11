from library import *
from get import Get


class Execution:
    @classmethod
    def login_as_member(cls):
        print("Enter your username and password:")
        muser = Get.get_string()
        mpass = Get.get_string()
        logout = True
        if not Library.mem_auth(muser, mpass):
            while True:
                print("Username or password incorrect \n (Retry or Enter '0' to Exit)")
                muser = input()
                if muser == "0":
                    logout = False
                    break
                mpass = input()
                if Library.mem_auth(muser, mpass):
                    break
        while logout:
            print("1.Logout")
            print("2.Borrow a book/journal")
            print("3.Return a book/journal")
            print("4.View all borrowed books")
            x = Get.get_int()
            if x == 1:
                logout = False
            elif x == 2:
                Library.print_line()
                Library.show_all()
                Library.print_line()
                print("Enter book/journal ID:")
                y = Get.get_int()
                Library.lib_borrow_book(y)
            elif x == 3:
                Library.print_line()
                print("(Enter the NUMBER of the book in this list:)")
                Library.borrowed()
                Library.print_line()
                print("Enter the book/journal Number:")
                z = Get.get_int()
                Library.lib_return_book(z)
            elif x == 4:
                Library.print_line()
                Library.borrowed()
                Library.print_line()

    @classmethod
    def login_as_manager(cls):
        print("Enter your username and password:")
        muser = Get.get_string()
        mpass = Get.get_string()
        logout = True
        if not Library.man_auth(muser, mpass):
            while True:
                print("Username or password incorrect \n (Retry or Enter '0' to Exit)")
                muser = input()
                if muser == "0":
                    logout = False
                    break
                mpass = input()
                if Library.man_auth(muser, mpass):
                    break
        while logout:
            print("1.Add a book")
            print("2.Add a member")
            print("3.View all members")
            print("4.View all books/journals")
            print("5.Delete a book by id")
            print("6.Logout")
            x = Get.get_int()
            if x == 1:
                Execution.add_book()
            elif x == 2:
                Execution.add_member()
            elif x == 3:
                Library.print_line()
                Execution.view_all_members()
                Library.print_line()
            elif x == 4:
                Library.print_line()
                Library.show_all()
                Library.print_line()
            elif x == 5:
                Library.print_line()
                Library.show_all()
                Library.print_line()
                print("Enter a book ID:")
                z = Get.get_int()
                Library.remove_book(z)
                Library.print_line()
            elif x == 6:
                logout = False

    @classmethod
    def add_book(cls):
        print("Enter new book's name")
        name = Get.get_string()
        print("Enter new book's writer's name")
        writer = Get.get_string()
        print("Enter new book's category")
        category = Get.get_string()
        print("Enter new book's ID")
        b_id = Get.get_int()
        print("Enter new book's stock count")
        stock = Get.get_int()
        Library.add_book(name, writer, category, b_id, stock)

    @classmethod
    def add_member(cls):
        print("Enter new member's username")
        new_user = Get.get_string()
        print("Enter new member's password")
        new_pass = Get.get_string()
        Library.add_member(new_user, new_pass)

    @classmethod
    def view_all_members(cls):
        for i in range(len(Library.members)):
            mem = Library.members[i]
            if mem is None:
                break
            print(f"name: {mem.get_user()} - ID: {mem.get_id()}")
