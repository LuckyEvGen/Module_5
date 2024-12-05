class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self,new_floor):
        if 1 < new_floor <= self.number_of_floor:
            for floors in range(1, new_floor + 1):
                print(floors)
        else:
            print('"Такого этажа не существует"')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(str(h1))
print(str(h2))
print(len(h1))
print(len(h2))
