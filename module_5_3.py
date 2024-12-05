class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 1 < new_floor <= self.number_of_floor:
            for floors in range(1, new_floor + 1):
                print(floors)
        else:
            print('"Такого этажа не существует"')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            #self.number_of_floor += value
            self.__add__(value)
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            #self.number_of_floor += value
            self.__add__(value)
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
