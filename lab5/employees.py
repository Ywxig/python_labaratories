"""
employees.py — модуль с определением классов Employee, HourlyEmployee, SalaryEmployee.
Демонстрирует инкапсуляцию (property() и декораторы) и наследование.
"""

import re
from datetime import date



def validate_name(value: str) -> str:
    """Имя — только буквы (латиница / кириллица), длина 2–50."""
    if not re.fullmatch(r"[A-Za-zА-Яа-яЁё]{2,50}", value):
        raise ValueError(f"Некорректное имя: '{value}'. Только буквы, 2–50 символов.")
    return value


def validate_phone(value: str) -> str:
    """Телефон в формате +373XXXXXXXX (8 цифр после +373)."""
    if not re.fullmatch(r"\+373\d{8}", value):
        raise ValueError(f"Некорректный телефон: '{value}'. Формат: +373XXXXXXXX")
    return value


def validate_birthday(value: str) -> str:
    """Дата рождения дд.мм.гггг; день 01-31, месяц 01-12, год 1960-2007."""
    if not re.fullmatch(r"(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(196\d|19[7-9]\d|200[0-7])", value):
        raise ValueError(
            f"Некорректная дата: '{value}'. Формат дд.мм.гггг; год 1960–2007."
        )
    return value


def validate_email(value: str) -> str:
    """
    Email: 2–20 символов (буквы, цифры, _.-) @ 4–7 букв . 2–4 буквы.
    """
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.\-]{1,19}@[A-Za-z]{4,7}\.[A-Za-z]{2,4}", value):
        raise ValueError(f"Некорректный email: '{value}'.")
    return value


def validate_specialty(value: str) -> str:
    """Специальность — только буквы, 4–20 символов."""
    if not re.fullmatch(r"[A-Za-zА-Яа-яЁё]{4,20}", value):
        raise ValueError(f"Некорректная специальность: '{value}'. 4–20 букв.")
    return value



class Employee:
    """
    Базовый класс сотрудника.

    Приватные атрибуты: __name, __phone, __birthday, __email, __specialty.
    Геттеры/сеттеры реализованы ДВУМЯ способами:
      • __name, __phone  — через функцию property()       (классический стиль)
      • __birthday, __email, __specialty — через @property  (декораторный стиль)
    """

    def __init__(self):
        self.__name = ""
        self.__phone = ""
        self.__birthday = ""
        self.__email = ""
        self.__specialty = ""

    #property() как функция

    def _get_name(self):
        return self.__name

    def _set_name(self, value):
        self.__name = validate_name(value)

    name = property(_get_name, _set_name,
                    doc="Имя сотрудника (только буквы, 2–50).")

    def _get_phone(self):
        return self.__phone

    def _set_phone(self, value):
        self.__phone = validate_phone(value)

    phone = property(_get_phone, _set_phone,
                     doc="Телефон в формате +373XXXXXXXX.")

    # декораторы @property

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = validate_birthday(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = validate_email(value)

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, value):
        self.__specialty = validate_specialty(value)

    # Публичные / защищённые методы

    def calculateAge(self) -> int:
        """Вычисляет возраст сотрудника в полных годах."""
        if not self.__birthday:
            return 0
        day, month, year = map(int, self.__birthday.split("."))
        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        return age

    def _calculateSalary(self):
        """Защищённый метод расчёта зарплаты (переопределяется в дочерних классах)."""
        pass

    def __str__(self):
        return (
            f"[Employee] {self.name} | тел: {self.phone} | "
            f"д.р.: {self.birthday} | email: {self.email} | "
            f"специальность: {self.specialty} | возраст: {self.calculateAge()}"
        )



class HourlyEmployee(Employee):
    """
    Почасовой сотрудник.
    Дополнительные приватные атрибуты: __hours_worked, __hourly_rate.
    """

    def __init__(self):
        super().__init__()
        self.__hours_worked = 0.0
        self.__hourly_rate = 0.0

    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Количество часов не может быть отрицательным.")
        self.__hours_worked = value

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Ставка должна быть положительным числом.")
        self.__hourly_rate = value

    def _calculateSalary(self) -> float:
        """Зарплата = отработанные часы × ставка за час."""
        return self.__hours_worked * self.__hourly_rate

    def __str__(self):
        base = super().__str__().replace("[Employee]", "[HourlyEmployee]")
        return (
            f"{base} | часов: {self.hours_worked} | "
            f"ставка/ч: {self.hourly_rate:.2f} MDL | "
            f"зарплата: {self._calculateSalary():.2f} MDL"
        )



class SalaryEmployee(Employee):
    """
    Наёмный сотрудник с фиксированной месячной зарплатой.
    Дополнительный приватный атрибут: __monthly_salary.
    """

    def __init__(self):
        super().__init__()
        self.__monthly_salary = 0.0

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Зарплата должна быть положительным числом.")
        self.__monthly_salary = value

    def _calculateSalary(self) -> float:
        """Зарплата = фиксированная месячная ставка по контракту."""
        return self.__monthly_salary

    def __str__(self):
        base = super().__str__().replace("[Employee]", "[SalaryEmployee]")
        return (
            f"{base} | месячная зарплата: {self._calculateSalary():.2f} MDL"
        )
