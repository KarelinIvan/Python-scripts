words = {}

# Открываем файл для чтения
with open("words.txt", "r", encoding="utf-8") as file:
    # Функция enumerate обходит каждое слово в файле,
    # создавая ключ:значение для записи в словарь words
    for key, value in enumerate(file):
        words[key] = value
