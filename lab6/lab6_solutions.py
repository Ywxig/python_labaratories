
# Лабораторная работа №6: Модули Time, DateTime, Calendar, Math, Tkinter

import datetime
import calendar
import math
import re
import time
import tkinter as tk
from tkinter import messagebox


# Задание 1. Рассчитать возраст в днях
# АЛГОРИТМ:
#   1. Запрашиваем у пользователя дату рождения в формате YYYY-MM-DD
#   2. Проверяем формат с помощью регулярного выражения
#   3. Преобразуем строку в объект datetime.date
#   4. Получаем сегодняшнюю дату через datetime.date.today()
#   5. Вычитаем дату рождения из сегодняшней даты — получаем объект timedelta
#   6. Из timedelta берём атрибут .days — это и есть количество прожитых дней

def zadanie_1():
    print("\n=== Задание 1: Возраст в днях ===")

    # Запрашиваем ввод в цикле, пока не введут корректную дату
    while True:
        date_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ")

        # Регулярное выражение проверяет формат: 4 цифры-2 цифры-2 цифры
        # ^ — начало строки, $ — конец строки
        # \d{4} — ровно 4 цифры (год), \d{2} — ровно 2 цифры (месяц/день)
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        if not re.match(pattern, date_str):
            print("Ошибка: неверный формат! Используйте ГГГГ-ММ-ДД")
            continue

        # Извлекаем год, месяц и день из строки
        year_of_birth  = int(date_str[:4])
        month_of_birth = int(date_str[5:7])
        day_of_birth   = int(date_str[8:10])

        # Проверяем, что такая дата реально существует
        try:
            birth_date = datetime.date(year_of_birth, month_of_birth, day_of_birth)
        except ValueError:
            print("Ошибка: такой даты не существует. Попробуйте снова.")
            continue

        # Убеждаемся, что дата рождения не в будущем
        today = datetime.date.today()
        if birth_date > today:
            print("Ошибка: дата рождения не может быть в будущем.")
            continue

        # Вычисляем разницу — операция над объектами date возвращает timedelta
        delta = today - birth_date  # тип: datetime.timedelta
        age_days = delta.days       # атрибут .days содержит количество дней

        print(f"Сегодня: {today}")
        print(f"Дата рождения: {birth_date}")
        print(f"Вы прожили {age_days} дней!")
        break



# Задание 2. Определение дня недели для определённой даты

# АЛГОРИТМ:
#   1. Запрашиваем у пользователя год, месяц и день (отдельно)
#   2. Используем calendar.weekday(year, month, day) — возвращает число 0..6
#      где 0 = понедельник, 6 = воскресенье (ISO-стандарт)
#   3. Переводим число в название дня недели на русском языке
#   4. Выводим результат

def zadanie_2():
    print("\n=== Задание 2: День недели для заданной даты ===")

    # Словарь для перевода номера дня в название на русском
    days_ru = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье"
    }

    try:
        year  = int(input("Введите год  (например, 2024): "))
        month = int(input("Введите месяц (1-12): "))
        day   = int(input("Введите день  (1-31): "))

        # calendar.weekday() — стандартная функция модуля calendar
        # Возвращает 0 (пн) … 6 (вс)
        weekday_number = calendar.weekday(year, month, day)
        weekday_name   = days_ru[weekday_number]

        print(f"\nДата {day:02d}.{month:02d}.{year} — это {weekday_name}.")
    except ValueError:
        print("Ошибка: введены некорректные данные.")



# Задание 3. Расчёт времени падения объекта

# АЛГОРИТМ:
#   1. Запрашиваем высоту h от пользователя
#   2. Проверяем, что введено число (не NaN, не строка, не отрицательное)
#      math.isnan() возвращает True, если значение не является числом (NaN)
#   3. Применяем формулу физики: t = sqrt(2h / g)
#      g = 9.8 м/с² (ускорение свободного падения)
#      math.sqrt() вычисляет квадратный корень
#   4. Выводим результат в секундах

def zadanie_3():
    print("\n=== Задание 3: Время падения объекта ===")

    G = 9.8  # ускорение свободного падения, м/с²

    while True:
        user_input = input("Введите высоту (в метрах): ")

        # Пробуем преобразовать строку в число с плавающей точкой
        try:
            h = float(user_input)
        except ValueError:
            print("Ошибка: введите числовое значение.")
            continue

        # math.isnan() — проверка на «не-число» (Not a Number, NaN)
        # Например, float('nan') даёт NaN; такое значение нельзя использовать
        if math.isnan(h):
            print("Ошибка: значение NaN недопустимо.")
            continue

        # Высота должна быть положительной
        if h <= 0:
            print("Ошибка: высота должна быть больше нуля.")
            continue

        # Формула: t = sqrt(2h / g)
        # math.sqrt() вычисляет квадратный корень из выражения
        t = math.sqrt(2 * h / G)

        print(f"\nВысота: {h} м")
        print(f"Ускорение свободного падения: {G} м/с²")
        print(f"Время падения: {t:.4f} секунд")
        break



# Задание 4 (авторское). Таймер обратного отсчёта с окном Tkinter

# ИДЕЯ: Пользователь задаёт количество секунд, нажимает «Старт»,
#        и видит обратный отсчёт в графическом окне.
#
# АЛГОРИТМ:
#   1. Создаём окно Tkinter (tk.Tk())
#   2. Добавляем поле ввода, метку-счётчик и кнопки
#   3. При нажатии «Старт» считываем количество секунд из поля ввода
#   4. Используем метод .after(ms, func) — встроенный планировщик Tkinter,
#      который вызывает func через ms миллисекунд (аналог time.sleep, но
#      не блокирует интерфейс)
#   5. На каждом шаге уменьшаем счётчик на 1 и обновляем метку
#   6. При достижении 0 показываем сообщение через messagebox

def zadanie_4():
    print("\n=== Задание 4: Таймер обратного отсчёта (Tkinter + time) ===")

    # --- Создание главного окна ---
    root = tk.Tk()
    root.title("Таймер обратного отсчёта")
    root.geometry("320x200")
    root.resizable(False, False)

    # Переменная Tkinter для хранения оставшихся секунд
    # tk.IntVar позволяет легко связывать виджеты с данными
    seconds_var = tk.IntVar(value=10)

    # Флаг: идёт ли сейчас отсчёт
    running = {"state": False}
    after_id = {"id": None}  # хранит ID задачи .after(), чтобы можно было отменить

    # --- Виджеты ---
    tk.Label(root, text="Введите секунды:").pack(pady=(15, 0))

    entry = tk.Entry(root, width=10, justify="center", font=("Arial", 14))
    entry.insert(0, "10")
    entry.pack()

    # Большая метка, показывающая оставшееся время
    label_time = tk.Label(root, text="--", font=("Arial", 36, "bold"), fg="navy")
    label_time.pack(pady=5)

    # --- Логика обратного отсчёта ---
    def tick(remaining):
        """Вызывается каждую секунду. Уменьшает счётчик и планирует следующий вызов."""
        if not running["state"]:
            return  # если нажали «Стоп», прекращаем

        label_time.config(text=str(remaining))

        if remaining <= 0:
            running["state"] = False
            label_time.config(text="0", fg="red")
            # time.strftime — форматируем текущее время для сообщения
            now = time.strftime("%H:%M:%S")
            messagebox.showinfo("Готово!", f"Время вышло!\nТекущее время: {now}")
            label_time.config(fg="navy")
            return

        # .after(1000, func) — запланировать вызов func через 1000 мс (1 сек)
        after_id["id"] = root.after(1000, tick, remaining - 1)

    def start():
        """Запускает таймер."""
        if running["state"]:
            return  # уже запущен

        try:
            secs = int(entry.get())
            if secs <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое положительное число!")
            return

        running["state"] = True
        label_time.config(fg="navy")
        tick(secs)  # первый вызов — сразу, остальные через .after()

    def stop():
        """Останавливает таймер."""
        running["state"] = False
        if after_id["id"]:
            root.after_cancel(after_id["id"])  # отменяем запланированный вызов
        label_time.config(text="--")

    # --- Кнопки ---
    frame_btns = tk.Frame(root)
    frame_btns.pack()
    tk.Button(frame_btns, text="Старт", width=8, bg="#4CAF50", fg="white",
              command=start).grid(row=0, column=0, padx=5)
    tk.Button(frame_btns, text="Стоп",  width=8, bg="#F44336", fg="white",
              command=stop).grid(row=0, column=1, padx=5)

    root.mainloop()



# Главное меню

def main():
    menu = {
        "1": ("Рассчитать возраст в днях",               zadanie_1),
        "2": ("Определить день недели для даты",          zadanie_2),
        "3": ("Рассчитать время падения объекта",         zadanie_3),
        "4": ("Таймер обратного отсчёта (Tkinter)",       zadanie_4),
        "0": ("Выход",                                    None),
    }

    while True:
        print("\n" + "="*50)
        print("  Лабораторная работа №6 — Главное меню")
        print("="*50)
        for key, (desc, _) in menu.items():
            print(f"  {key}. {desc}")

        choice = input("\nВыберите задание: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
