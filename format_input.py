import re


def formatter_str():
    """
    Функция для обработки строк.
    Если строка начинается с ! знака, то вся строка приводится к верхнему регистру. Иначе к нижнему регистру.
    После преведения к регистру из строки удаляются символы "!@#%"
    """
    while True:
        line = input()

        if not line:
            print("Данные отсутствуют")
            return

        format_line = ""

        if line[0] == "!":
            format_line = line.upper()
        else:
            format_line = line.lower()

        # с помощью модуля re, формируем список удаляемых символов
        pattern = r"[!@#%]"
        cleaned_line = re.sub(pattern, "", format_line)

        print(cleaned_line)


formatter_str()
