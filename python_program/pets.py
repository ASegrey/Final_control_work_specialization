from animals import Animals


class Pet(Animals):
    """Класс домашних животных"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)


class Cat(Pet):
    """Класс кошка"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)

    def __str__(self):
        return f"Кошка по кличке {self.get_name()}, возраст {self.get_age()}, умеет: {self.get_command()}"


class Dog(Pet):
    """Класс Собака"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)

    def __str__(self):
        return f"Собака по кличке {self.get_name()}, возраст {self.get_age()}, умеет: {self.get_command()}"


class Hamster(Pet):
    """Класс хомяк"""

    def __init__(self, name, age, command):
        super().__init__(name, age, command)

    def __str__(self):
        return f"Собака по кличке {self.get_name()}, возраст {self.get_age()}, умеет: {self.get_command()}"
