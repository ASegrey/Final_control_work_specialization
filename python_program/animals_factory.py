from exeptions import CountException
from pets import Cat,Dog,Hamster
from pack_animal import Horse,Camel,Donkey


class Count:
    count = 0

    def __init__(self):
        type(self).count = 0

    def add(self):
        self.count += 1

    def get_counter(self):
        return self.count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if AnimalFactory.count.get_counter() == 0:
            raise CountException()
        

class AnimalFactory:
    count = Count()
    classes_list = ["Кошка", "Собака", "Хомяк", "Лошадь", "Верблюд", "Осёл"]
    registry = dict.fromkeys(classes_list, [])

    def __init__(self, classes, name, age, commands):
        """
        Создает экземпляр животного на основе переданного типа и параметров.
        Добавляет к словарю по типам животных
        """
        animal_classes = {
            'Кошка': Cat,
            'Собака': Dog,
            'Хомяк': Hamster,
            'Лошадь': Horse,
            'Верблюд': Camel,
            'Осёл': Donkey
        }
        self.classes = classes
        self.name = name
        self.age = age
        self.commands = commands
        if self.classes in animal_classes:
            AnimalFactory.registry[self.classes] = (AnimalFactory.registry.setdefault(self.classes, []) +
                                                    [animal_classes[self.classes](self.name, self.age, self.commands)])
        else:
            raise ValueError(f"Неизвестный тип животного: {self.classes}")
        