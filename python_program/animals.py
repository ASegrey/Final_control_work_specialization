class Animals:
    """Родительский класс животных"""

    def __init__(self, name: str, age: int, command: str = None):
        self.name = name
        self.age = age
        self.command = command

    def set_commands(self, command):
        self.command = command

    def set_name(self, name):
        self.name = name

    def get_command(self):
        return self.command

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age