from pathlib import Path
from registry_file import load_animal_json, save_animal_json
from exeptions import CountException
from menu_program import run


if __name__ == '__main__':
    load_animal_json(Path("animal_reg.json"))
    try:
        run()
    except CountException as exp:
        raise SystemExit('Ошибка, счетчик не был использован в блоке try-with-resources')
    finally:
        save_animal_json(Path("animal_reg.json"))
        print("Выход из приложения")