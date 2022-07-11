from get import Get
from library import *
from execution import Execution

Library.read_data()
Library.set_manager("admin", "admin")
while True:
    print("1.Login as a member")
    print("2.Login as a manager")
    print("3.Exit")
    p = Get.get_int()

    if p == 1:
        Execution.login_as_member()
    elif p == 2:
        Execution.login_as_manager()
    elif p == 3:
        Library.write_data()
        break
    else:
        print("!please enter a valid Number! \n")
