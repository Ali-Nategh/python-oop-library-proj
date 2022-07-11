class Inscription:
    def __init__(self, name, category):
        self.name = name
        self.category = category


class Book(Inscription):
    def __init__(self, name, writer, category, b_id, stock_count):
        super().__init__(name, category)
        self.writer = writer
        self.b_id = b_id
        self.stock_count = stock_count

    def get_name(self):
        return self.name

    def get_writer(self):
        return self.writer

    def get_category(self):
        return self.category

    def get_id(self):
        return self.b_id

    def get_stock(self):
        return self.stock_count


class Journal(Inscription):
    def __init__(self, name, j_num, p_date, category, j_id, stock_count):
        super().__init__(name, category)
        self.j_num = j_num
        self.p_date = p_date
        self.j_id = j_id
        self.stock_count = stock_count

    def get_name(self):
        return self.name

    def get_num(self):
        return self.j_num

    def get_date(self):
        return self.p_date

    def get_category(self):
        return self.category

    def get_id(self):
        return self.j_id

    def get_stock(self):
        return self.stock_count
