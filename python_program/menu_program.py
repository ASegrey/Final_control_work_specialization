from animals_factory import AnimalFactory

def list_program():
    print('\n Выберите пункт меню: '
          '\n 1 - посмотреть реестр животых'
          '\n 2 - добавление нового животного в реестр'
          '\n 3 - добавление новой команды животному'
          '\n 4 - посмотреть список команд животного'
          '\n 0 - выход')


def run():
    while True:
        list_program()
        command = input('Введите номер пункта меню: ')
        if command == '1':
            show_animals()
        elif command == '2':
            add_animals()
        elif command == '3':
            add_commands()
        elif command == '4':
            show_commands()
        elif command == '0':
            with AnimalFactory.count:
                break
        else:
            print('Ошибка ввода номера пункта меню')


def show_animals():
    print('Просмотр всех животных в реестре')
    list_str = "_________________________________" + '\n'
    for key in AnimalFactory.registry:
        list_str += 'Животное ' + key + ':\n'
        for animal in AnimalFactory.registry[key]:
            list_str += str(animal) + '\n'
        list_str += "_________________________________" + '\n'
    print(f"{list_str}")
    input('Для выхода в меню, введите любое значение -> ')


def input_classes() -> str:
    text = ''
    for item in AnimalFactory.classes_list:
        text += item + "; "
    text = text[:-2]
    while True:
        classes = input(f"Введите тип животного из списка [{text}] \n -> ").capitalize()
        if classes in AnimalFactory.classes_list:
            return classes


def input_name(classes):
    text = ''
    for item in AnimalFactory.registry[classes]:
        text += item.get_name() + "; "
    text = text[:-2]
    while True:
        name = input(f"Введите имя животного из списка [{text}] \n -> ").capitalize()
        for item in AnimalFactory.registry[classes]:
            if item.get_name() == name:
                return name, item.get_age(), item.get_command()


def input_command():
    commands_save = ""
    while True:
        commands = input(f"Введите команду или несколько команд через запятую, для животного -> ")
        command_list = commands.split(",")
        for command in command_list:
            if command[0] == " ":
                command = command[1:]
            if not command.isalpha():
                print('Ошибка! Команда должна быть написана буквами')
                break
            else:
                if len(commands_save) > 0:
                    commands_save += ","
                commands_save += command.capitalize()
        else:
            return commands_save


def input_name_command():
    while True:
        name = input(f"Введите имя животного -> ").capitalize()
        if name.isalpha():
            while True:
                age = input(f"Введите возраст животного (целое число) -> ")
                if age.isdigit():
                    age = int(age)
                    return name, age, input_command()
                else:
                    print('Ошибка! Возраст может быть только целым числом!')
        else:
            print('Ошибка! Имя должно содержать только буквы')


def add_animals():
    classes = input_classes()
    while True:
        name, age, commands = input_name_command()
        AnimalFactory(classes, name, age, commands)
        with AnimalFactory.count:
            AnimalFactory.count.add()
        print(f'Животное {classes}, с именем {name} добавлено!')
        output = input(f"Добавить еще одно животное {classes} ? (да/__) ->").capitalize()
        if not output == "Да":
            break


def add_commands():
    classes = input_classes()
    name, age, commands = input_name(classes)
    commands_add = input_command()
    if len(commands) > 0:
        commands += ","
    commands += commands_add
    for item in AnimalFactory.registry[classes]:
        if item.get_name() == name and item.get_age() == age:
            item.set_commands(commands)
    print(f'Животному {classes}, с именем {name}, добавлены команды: {commands_add}')


def show_commands():
    classes = input_classes()
    name, _, command = input_name(classes)
    print(f'Животное {classes}, с именем {name}, умеет выполнять команды: {command}')