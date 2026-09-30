import re


def standardise_number(phone_number: str) -> str:
    """Функция принимает строку с номером мобильного телефона
    и приводит к единому формату записи +7(XXX)XXX-XX-XX"""

    numbers = []

    # Создаем флаг для проверки
    has_letters = False
    # Проверяем не содержит ли строка быквы
    for i in phone_number:
        if i.isalpha():
            has_letters = True

    if has_letters == True:
        raise ValueError("Ошибка, в номере телефона не должно быть букв.")
    else:
        line = phone_number
        # Очищаем строку от символов, оставляем только цифры
        line_clean = re.sub(r"\D", "", line)
        numbers = list(line_clean)

        if len(numbers) == 11:
            if numbers[0] == "8":
                numbers[0] = "7"
            phone = "".join(numbers)
            formatter = (
                f"+{phone[0]}({phone[1:4]}){phone[4:7]}" f"-{phone[7:9]}-{phone[9:11]}"
            )
            return formatter
        elif len(numbers) > 11:
            raise ValueError(
                "Неверный формат мобильного номера телефлна РФ,"
                "номер должен состоять из 11 цифр."
                "Введено более 11 цифр"
            )
        elif len(numbers) < 11:
            raise ValueError(
                "Неверный формат мобильного номера телефлна РФ,"
                "номер должен состоять из 11 цифр."
                "Введено менее 11 цифр"
            )


# --- Блок тестирования ---
if __name__ == "__main__":
    test_cases = [
        "+79649571623",  # Корректный
        "8(911)675-94 61",  # Содержит пробелы и символы между цифрами,
        # обрабатывается программой удаляя символы и пробелы
        "89116784av4",  # Содержит буквы
        "8 911 458 45 789",  # Слишком длинный
        "8(999) 489 12 1",  # Слишеом короткий
    ]

    for test in test_cases:
        print("Начинаем проверку")
        print(f"Проверяем ошибки ввода: {test}")
        try:
            result = standardise_number(test)
            print("Успешно обработано программой.")
        except ValueError as e:
            print(f"Ошибка ввода данных: {e}")
