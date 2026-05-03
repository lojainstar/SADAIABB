from sho3a3 import Sho3a3

class Masfofah:
    def __init__(self, sho3a3s: list):
        self.rows = [Sho3a3(row) for row in sho3a3s]
        self.shaper = (len(self.rows), len(self.rows[0]))

    def __repr__(self):
        return "masfofah:\n" + "\n".join(str(r) for r in self.rows)

    def shape(self):
        return self.shaper

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i):
        return self.rows[i]

    # ✅ جمع
    def __add__(self, other):
        assert self.shape() == other.shape()
        return Masfofah([self[i] + other[i] for i in range(len(self))])

    # ✅ طرح
    def __sub__(self, other):
        assert self.shape() == other.shape()
        return Masfofah([self[i] - other[i] for i in range(len(self))])

    # ✅ استخراج الأعمدة
    def extract_columns(self):
        cols = []
        rows, cols_count = self.shape()

        for j in range(cols_count):
            col = [self[i][j] for i in range(rows)]
            cols.append(col)

        return Masfofah(cols)

    # ✅ ضرب المصفوفات
    def __mul__(self, other):
        assert self.shape()[1] == other.shape()[0]

        result = []
        cols = other.extract_columns()

        for row in self.rows:
            new_row = []
            for col in cols.rows:
                new_row.append(row * col)  # dot product
            result.append(new_row)

        return Masfofah(result)

    # ✅ المنقول
    def man8ool(self):
        return self.extract_columns()

    # ✅ المجموع
    def sum(self, axis):
        rows, cols = self.shape()

        if axis == 0:
            result = []
            for j in range(cols):
                s = sum(self[i][j] for i in range(rows))
                result.append(s)
            return Masfofah([result])

        elif axis == 1:
            result = []
            for i in range(rows):
                result.append(sum(self[i]))
            return Masfofah([result])

    # ✅ إضافة
    def add(self, other, axis=0):
        if axis == 0:
            for i in range(len(self)):
                self[i].sho3a3 += other[i].sho3a3

        elif axis == 1:
            self.rows += other.rows

        self.shaper = (len(self.rows), len(self.rows[0]))
   