# Доработаем задачи 5-6. Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните его из
# класса-фабрики.


class Animals:
    def __init__(self, name):
        self.name = name


class Fish(Animals):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def unic_info(self):
        return f'для {self.name}: глубина {self.depth}'


class Bird(Animals):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def unic_info(self):
        return f'для {self.name}: размах {self.wingspan}'


class Mammals(Animals):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def unic_info(self):
        return f'для {self.name}: Bec {self.weight}'


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        if animal_type == "Fish":
            return Fish(*args, **kwargs)
        elif animal_type == "Bird":
            return Bird(*args, **kwargs)
        elif animal_type == "Mammal":
            return Mammals(*args, **kwargs)
        else:
            raise ValueError("Недопустимый тип животного")


factory = AnimalFactory()  # factory  method

fish = factory.create_animal("Fish", "Flounder", 100)
bird = factory.create_animal("Bird", "Tweety", 0.1)
mammal = factory.create_animal("Mammal", "Leon", 650)

print(fish.unic_info())
print(bird.unic_info())
print(mammal.unic_info())

print("*" * 50)

fish = Fish('Nemo', 1000)
bird = Bird('Woody', 2)
mammal = Mammals('mouse', 0.2)

print(fish.unic_info())
print(bird.unic_info())
print(mammal.unic_info())
