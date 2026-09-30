import re

list_words = []
print(type(list_words))

# Читаем файл, убираем знаки преписания и записываем слова в список list_words
with open("pg79633.txt", "r", encoding="utf-8") as file:
    line = file.read()
    # Переменная со знаками препинания, которые удаляем из текста,
    # приводим все к нижнему регистру
    patterns = r"[!,.?;:#$%^&*(),]"
    clear_line = re.sub(patterns, "", line).lower()

    list_words = clear_line.split()

col_words = len(list_words)
print(f"Количество слов в книге:{col_words}")

unique_words = set()

# Перебираем слова из списка и добавляем во множество,
# таким образом получаем только уникальные слова из текста
for i in list_words:
    unique_words.add(i)

col_uni_words = len(unique_words)
print(f"Количество уникальных слов в книге:{col_uni_words}")
