# ___задача 1___
# Определяем список
programming_languages = ["Python", "Java", "C++", "JavaScript", "Rust"]

# 1. Вывод 1-го и 3-го значений (индексы 0 и 2)
print(f"Первый: {programming_languages[0]}, Третий: {programming_languages[2]}")

# 2. Замена значения
programming_languages[1] = "Kotlin"

# 3. Срез элементов (со 2-го по 4-й не включая)
print("Срез:", programming_languages[1:3])

# 4. Применение инструментов:
# Метод: .append() — добавляет в конец
programming_languages.append("Go") 

# Функции: len() и sorted()
print("Длина:", len(programming_languages))
print("Отсортирован:", sorted(programming_languages))

# Операторы: +, *, in
new_list = programming_languages + ["Swift"] # + (конкатенация)
doubled = ["A"] * 2                          # * (дублирование)
print("Есть ли Rust?", "Rust" in programming_languages) # in (проверка)

# Определяем кортеж
coordinates = (10, 20, 30, 40, 50)


# ___задача 2___
# 1. Из строки в число
price_str = "150"
price_int = int(price_str) # Теперь можно считать: price_int + 10

# 2. Из списка в множество (для удаления дубликатов)
raw_data = [1, 2, 2, 3, 3, 3]
clean_data = list(set(raw_data)) # [1, 2, 3]

# 3. Из числа в строку (для вывода)
age = 25
message = "Возраст: " + str(age)


# ___задача 3___
# 1. Проверка типа данных
print(f"Тип данных: {type(coordinates)}")

# 2. Первое и последнее значения
print(f"Первое: {coordinates[0]}, Последнее: {coordinates[-1]}")

# 3. Срез
print("Срез (первые три):", coordinates[:3])

# 4. Три функции: max(), min(), sum()
print(f"Макс: {max(coordinates)}, Мин: {min(coordinates)}, Сумма: {sum(coordinates)}")

# Определяем множество с повторами
unique_codes = {101, 102, 103, 101, 105, 102}

# Вывод на экран
print("Множество:", unique_codes)


# ___задача 4___
# Словарь с текстовыми ключами
user_info = {"name": "Alice", "role": "Admin", "id": 777}
# Словарь с числовыми ключами
error_codes = {404: "Not Found", 500: "Server Error"}

# Доступ к элементам
print(f"Имя: {user_info['name']}, Ошибка 404: {error_codes[404]}")

# 3 метода: .keys(), .values(), .get()
print(user_info.keys())    # Все ключи
print(user_info.values())  # Все значения
print(user_info.get("age", "Не найдено")) # Безопасное получение

# 2 функции: len(), list()
print("Количество ключей:", len(user_info))
print("Ключи списком:", list(error_codes))