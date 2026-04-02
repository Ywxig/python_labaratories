"""
main.py — основная программа.
Импортирует модуль employees, создаёт 6 объектов (2 + 2 + 2),
запрашивает данные через input() с валидацией, выводит результаты.
"""

from employees import Employee, HourlyEmployee, SalaryEmployee


def safe_input(prompt: str, obj, setter_name: str) -> None:
    """
    Повторяет запрос до тех пор, пока значение не пройдёт валидацию.
    setter_name — имя свойства (строка), например 'name'.
    """
    while True:
        value = input(prompt).strip()
        try:
            setattr(obj, setter_name, value)
            break
        except ValueError as e:
            print(f"  ✗ Ошибка: {e}")


def safe_float_input(prompt: str, obj, setter_name: str) -> None:
    """Аналог safe_input для числовых полей."""
    while True:
        value = input(prompt).strip()
        try:
            setattr(obj, setter_name, value)
            break
        except (ValueError, TypeError) as e:
            print(f"  ✗ Ошибка: {e}")

def fill_base(obj: Employee, label: str) -> None:
    """Запрашивает базовые поля Employee."""
    print(f"\n{'─'*50}")
    print(f"  Ввод данных: {label}")
    print(f"{'─'*50}")
    safe_input("  Имя           : ", obj, "name")
    safe_input("  Телефон       : ", obj, "phone")
    safe_input("  Дата рождения : ", obj, "birthday")
    safe_input("  Email         : ", obj, "email")
    safe_input("  Специальность : ", obj, "specialty")


def fill_hourly(obj: HourlyEmployee, label: str) -> None:
    """Запрашивает базовые + почасовые поля."""
    fill_base(obj, label)
    safe_float_input("  Часов отработано  : ", obj, "hours_worked")
    safe_float_input("  Ставка за час MDL : ", obj, "hourly_rate")


def fill_salary(obj: SalaryEmployee, label: str) -> None:
    """Запрашивает базовые + поле месячной зарплаты."""
    fill_base(obj, label)
    safe_float_input("  Месячная зарплата MDL : ", obj, "monthly_salary")


print("=" * 60)
print("   СИСТЕМА УЧЁТА СОТРУДНИКОВ")
print("=" * 60)

# 2 объекта Employee
emp1 = Employee()
emp2 = Employee()
fill_base(emp1, "Employee #1")
fill_base(emp2, "Employee #2")

# 2 объекта HourlyEmployee
hourly1 = HourlyEmployee()
hourly2 = HourlyEmployee()
fill_hourly(hourly1, "HourlyEmployee #1")
fill_hourly(hourly2, "HourlyEmployee #2")

# 2 объекта SalaryEmployee
salary1 = SalaryEmployee()
salary2 = SalaryEmployee()
fill_salary(salary1, "SalaryEmployee #1")
fill_salary(salary2, "SalaryEmployee #2")



all_objects = [emp1, emp2, hourly1, hourly2, salary1, salary2]

print("\n" + "=" * 60)
print("   ДАННЫЕ ВСЕХ СОТРУДНИКОВ (геттеры)")
print("=" * 60)

for obj in all_objects:
    print(obj)

# Подробный вывод через геттеры (наглядно для преподавателя)
print("\n" + "=" * 60)
print("   ПОДРОБНЫЙ ВЫВОД ЧЕРЕЗ ГЕТТЕРЫ")
print("=" * 60)

for i, obj in enumerate(all_objects, 1):
    print(f"\n  Объект #{i} ({type(obj).__name__})")
    print(f"    name       = {obj.name}")
    print(f"    phone      = {obj.phone}")
    print(f"    birthday   = {obj.birthday}")
    print(f"    email      = {obj.email}")
    print(f"    specialty  = {obj.specialty}")
    print(f"    age        = {obj.calculateAge()}")
    if isinstance(obj, HourlyEmployee):
        print(f"    hours      = {obj.hours_worked}")
        print(f"    rate/h     = {obj.hourly_rate}")
    if isinstance(obj, SalaryEmployee):
        print(f"    monthly    = {obj.monthly_salary}")


print("\n" + "=" * 60)
print("   ЗАРПЛАТЫ ПО ТИПУ НАЙМА")
print("=" * 60)

employees_list = [emp1, emp2]
hourly_list    = [hourly1, hourly2]
salary_list    = [salary1, salary2]

print("\n  Employee (базовый — зарплата не определена):")
print("  ", [f"{e.name}: —" for e in employees_list])

print("\n  HourlyEmployee (почасовые):")
print("  ", [f"{e.name}: {e._calculateSalary():.2f} MDL" for e in hourly_list])

print("\n  SalaryEmployee (фиксированная зарплата):")
print("  ", [f"{e.name}: {e._calculateSalary():.2f} MDL" for e in salary_list])

print("\n" + "=" * 60)
print("   ГОТОВО")
print("=" * 60)
