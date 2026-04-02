# main.py — главный файл программы "Подарки всем"
# Импортируем функции из модуля functions.py

from functions import input_employee_data, view_children_data, view_childless_employees


def show_menu():
    """Выводит главное меню."""
    print("\n" + "=" * 40)
    print("     Компания 'Подарки всем'")
    print("=" * 40)
    print("  1. Ввод данных сотрудника")
    print("  2. Просмотр данных о детях")
    print("  3. Список бездетных сотрудников")
    print("  4. Выход")
    print("=" * 40)


def main():
    """Основной цикл программы."""
    while True:
        show_menu()
        choice = input("Выберите пункт меню (1–4): ").strip()

        if choice == "1":
            input_employee_data()
        elif choice == "2":
            view_children_data()
        elif choice == "3":
            view_childless_employees()
        elif choice == "4":
            print("До свидания! ")
            break
        else:
            print("  Неверный выбор. Введите число от 1 до 4.")


if __name__ == "__main__":
    main()
