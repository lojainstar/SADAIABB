class Sho3a3:
    def __init__(self, numbers: list):
        self.sho3a3 = numbers
        
        self._shape = (1, len(numbers))
def __len__(self):
    return len(self.sho3a3)
    def __repr__(self) -> str:
        return f"sho3a3:{self.sho3a3}"

    def __str__(self) -> str:
        return self.__repr__()
if __name__ == "__main__":
    s = Sho3a3([1, 2, 3])
    print(s)

    def __len__(self) -> int:
        return len(self.sho3a3)

    def __iter__(self):
        return iter(self.sho3a3)

    def __getitem__(self, placement):
        return self.sho3a3[placement]

    def __setitem__(self, placement, value):
        self.sho3a3[placement] = value
            # ✅ الجمع
    def __add__(self, other):
        if isinstance(other, Sho3a3):
            assert len(self) == len(other)
            return Sho3a3([a + b for a, b in zip(self, other)])
        else:
            return Sho3a3([a + other for a in self])

    def __radd__(self, other):
        return self.__add__(other)

    # ✅ الطرح
    def __sub__(self, other):
        if isinstance(other, Sho3a3):
            assert len(self) == len(other)
            return Sho3a3([a - b for a, b in zip(self, other)])
        else:
            return Sho3a3([a - other for a in self])

    def __rsub__(self, other):
        return Sho3a3([other - a for a in self])

    # ✅ الضرب
    def __mul__(self, other):
        if isinstance(other, Sho3a3):
            assert len(self) == len(other)
            return sum(a * b for a, b in zip(self, other))
        else:
            return Sho3a3([a * other for a in self])

    def __rmul__(self, other):
        return self.__mul__(other)

    # ✅ دوال مساعدة
    def shape(self):
        return self._shape

    def sum(self):
        return sum(self.sho3a3)

    def element_wise_product(self, other):
        assert len(self) == len(other)
        for i in range(len(self)):
            self[i] *= other[i]