from some_file import programming_languages

print(f"Hello user, welcome to the world of Python programming!")
name = input("Please enter your name: ")
print(f"Nice to meet you, {name}! Let's get started with some Python basics.")

# This is a one string comment in Python
"""
This is documenr string or multi-line comment in Python.
"""

int_var = 10
float_var = 3.14
user_status = "Online"
long_string = """Определите 4 переменные, используя правильные названия для них в Python. Присвойте
каждой из них, последовательно: числовое целое значение, вещественное значение,
короткое текстовое значение, текстовое значение, которое занимает 3-4 строки.
6. Выведите на экран тип данных для двух определенных ранее переменных."""

print(f"The integer variable is: {int_var} and its type is: {type(int_var)}")
print(f"The float variable is: {float_var} and its type is: {type(float_var)}")

print(f"The length of your name is {len(name)} characters.")

print(f"Your name in lowercase is: {name.lower()}")

upper_name = name.upper()

print(f"{name[0:2]} - these are the first two characters of your name.")


#task 4;

prices = [150, 2100, 45]
products = ["Кофе", "Смартфон", "Ручка"]

info = "Список покупок:\n- {0}: {1} руб.\n- {2}: {3} руб.\n- {4}: {5} руб.".format(
    products[0], prices[0], 
    products[1], prices[1], 
    products[2], prices[2]
)

print(info)

# 1. Get user input and convert it to an integer
user_input = input("Введите ваш возраст (целое число): ")
age = int(user_input)
age_in_ten_years = age + 10

result_text = "Сейчас вам " + str(age) + ", а через 10 лет вам будет " + str(age_in_ten_years) + "!"

print(result_text)

registered_emails = ["admin@mail.ru", "user@mail.ru"]
new_email = "guest@mail.ru"

is_unique = new_email not in registered_emails

print("Можно зарегистрировать:", is_unique)

if "Python" in programming_languages:
    print("U are not coder cuz u know python :)")
