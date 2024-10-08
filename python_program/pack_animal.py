from animals import Animals


class PackAnimal(Animals):
    """Класс домашних животных"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)


class Horse(PackAnimal):
    """Класс лошадь"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)

    def __str__(self):
        return f"Лошадь по кличке {self.get_name()}, возраст {self.get_age()}, умеет: {self.get_command()}"


class Camel(PackAnimal):
    """Класс Верблюды"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)

    def __str__(self):
        return f"Верблюд по кличке {self.get_name()}, возраст {self.get_age()}, умеет: {self.get_command()}"


class Donkey(PackAnimal):
    """Класс Ослы"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)

    def __str__(self):
        return f"Осёл по кличке {self.get_name()}, возраст {self.get_age()}, умеет: {self.get_command()}"
