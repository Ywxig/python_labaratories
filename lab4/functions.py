# functions.py — модуль с функциями для учёта данных о детях сотрудников

import re

DATA_FILE = "data.txt"

# Имя/Фамилия: только буквы, 2–20 символов, один дефис между частями разрешён
NAME_PATTERN = re.compile(
    r'^[A-Za-zА-Яа-яЁёÎîȘșȚț]{2,20}'
    r'(-[A-Za-zА-Яа-яЁёÎîȘșȚț]{2,20})*$'
)

# Отдел: буквы и цифры, между ними не более одного пробела
DEPT_PATTERN = re.compile(
    r'^[A-Za-zА-Яа-яЁёÎîȘșȚț0-9]+'
    r'( [A-Za-zА-Яа-яЁёÎîȘșȚț0-9]+)*$'
)

# Количество детей: целое число от 0 до 19
CHILDREN_PATTERN = re.compile(r'^(1[0-9]|[0-9])$')

def input_employee_data():
    """Запрашивает данные сотрудника, проверяет их и сохраняет в файл."""
    print("\n--- Ввод данных сотрудника ---")

    while True:
        last_name  = input("Фамилия: ").strip()
        first_name = input("Имя: ").strip()
        department = input("Отдел: ").strip()
        children   = input("Количество детей (0–19): ").strip()

        errors = []

        if not NAME_PATTERN.match(last_name):
            errors.append("Фамилия: только буквы (2–20), допускается один дефис между частями.")
        if not NAME_PATTERN.match(first_name):
            errors.append("Имя: только буквы (2–20), допускается один дефис между частями.")
        if not DEPT_PATTERN.match(department):
            errors.append("Отдел: буквы и цифры, не более одного пробела между словами.")
        if not CHILDREN_PATTERN.match(children):
            errors.append("Количество детей: целое число от 0 до 19.")

        if errors:
            print("\n  Обнаружены ошибки:")
            for err in errors:
                print(f"   • {err}")
            print("Пожалуйста, введите данные заново.\n")
            continue  # возврат к вводу

        # Замена пробела в названии отдела на подчёркивание
        department_saved = department.replace(" ", "_")

        # Сохранение в файл
        try:
            with open(DATA_FILE, "a", encoding="utf-8") as f:
                f.write(f"{last_name}\t{first_name}\t{department_saved}\t{children}\n")
            print(f" Данные сотрудника {last_name} {first_name} сохранены.")
        except IOError as e:
            print(f" Ошибка записи в файл: {e}")

        break  # данные введены корректно — выходим из цикла

def view_children_data():
    """Выводит список всех сотрудников и суммарное количество детей."""
    print("\n--- Список сотрудников и количество детей ---")

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("  Файл данных не найден. Сначала введите данные.")
        return

    if not lines:
        print("Файл пуст.")
        return

    total_children = 0
    print(f"\n{'№':<4} {'Фамилия':<20} {'Имя':<20} {'Отдел':<20} {'Детей'}")
    print("-" * 72)

    for idx, line in enumerate(lines, start=1):
        parts = line.strip().split("\t")
        if len(parts) != 4:
            continue  # пропускаем некорректные строки

        last_name, first_name, department, children_str = parts
        try:
            children = int(children_str)
        except ValueError:
            children = 0

        total_children += children
        dept_display = department.replace("_", " ")
        print(f"{idx:<4} {last_name:<20} {first_name:<20} {dept_display:<20} {children}")

    print("-" * 72)
    print(f"{'Итого детей (подарков для Деда Мороза):':<56} {total_children}")


def view_childless_employees():
    """Выводит список сотрудников без детей."""
    print("\n--- Сотрудники без детей ---")

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(" Файл данных не найден. Сначала введите данные.")
        return

    childless = []
    for line in lines:
        parts = line.strip().split("\t")
        if len(parts) != 4:
            continue
        last_name, first_name, _, children_str = parts
        try:
            if int(children_str) == 0:
                childless.append((last_name, first_name))
        except ValueError:
            pass

    if not childless:
        print("Все сотрудники имеют детей (или данные не введены).")
        return

    print(f"\n{'№':<4} {'Фамилия':<20} {'Имя'}")
    print("-" * 44)
    for idx, (last_name, first_name) in enumerate(childless, start=1):
        print(f"{idx:<4} {last_name:<20} {first_name}")
    print(f"\nВсего бездетных сотрудников: {len(childless)}")
