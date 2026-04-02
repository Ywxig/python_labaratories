import re

def validate_phone():
    """
    Проверяет введённый номер телефона на соответствие молдавскому формату.
    Допустимые форматы:
      - 0037399999999  (13 цифр с кодом 00373)
      - +37399999999   (11 цифр с кодом +373)
      - 99999999       (8 цифр)
      - 099999999      (0 и 8 цифр = 9 цифр)
    """
    pattern = re.compile(
        r'^(0037[3-9]\d{8}|'   # 0037X + 8 цифр (X от 3 до 9)
        r'\+37[3-9]\d{8}|'     # +37X + 8 цифр
        r'[1-9]\d{7}|'         # 8 цифр (не начинается с 0)
        r'0\d{8})$'            # 0 + 8 цифр = 9 цифр
    )

    while True:
        try:
            phone = input("Введите номер телефона: ").strip()

            if not phone:
                raise ValueError("Номер телефона не может быть пустым.")

            if pattern.match(phone):
                print(f" Номер '{phone}' корректен! Отличный ввод!")
                break
            else:
                print(" Неверный формат. Допустимые форматы:")
                print("   0037373XXXXXXX  /  +37373XXXXXXX  /  XXXXXXXX  /  0XXXXXXXX")

        except ValueError as e:
            print(f"  Ошибка: {e}")
        except KeyboardInterrupt:
            print("\nВвод прерван пользователем.")
            break

if __name__ == "__main__":
    validate_phone()
