class Get:
    @classmethod
    def get_int(cls):
        while True:
            try:
                inp = int(input())
            except Exception:
                print("!please enter a valid Integer")
            else:
                break
        return inp

    @classmethod
    def get_string(cls):
        while True:
            try:
                inp = input()
                x = int(inp)
            except Exception:
                break
            else:
                print("!please enter a valid String")
        return inp
