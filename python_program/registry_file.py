import json
from pathlib import Path
from animals_factory import AnimalFactory


def load_animal_json(file: Path) -> None:
    if file.is_file():
        with open(file, "r", encoding="utf-8") as f_read:
            reg = json.load(f_read)
            for classes, animals in reg.items():
                for animal in animals:
                    AnimalFactory(classes, animal[0], animal[1], animal[2])


def save_animal_json(file: Path) -> None:
    saver = {}
    for classes in AnimalFactory.classes_list:
        for animal in AnimalFactory.registry[classes]:
            saver[classes] = saver.setdefault(classes, []) + [
                [animal.get_name(), animal.get_age(), animal.get_command()]]
    if len(saver) > 0:
        with open(file, "w", encoding="utf-8") as f_write:
            json.dump(saver, f_write, ensure_ascii=False, indent=4)