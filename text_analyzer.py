import re
from collections import Counter

# Принимаем строку и приводим к нижнему регистру методом lower
line = str(input()).lower()

# Убираем из строки символы (перечисляем в переменной pattern), для форматирования используем модуль re
pattern = r"[!,.?;:#$%^&*(),]"
cleaned_str = re.sub(pattern, "", line)

# резделяем строку на слова методом split(по умолчанию через пробел)
list_words = cleaned_str.split()

# создаем счётчик поторяющихся слов, используем класс Counter из модуля collections
word_counter = Counter(list_words)
filter_words = []

for word in word_counter:
    # пропускаем слова длинной менее 5 символов
    if len(word) < 5:
        continue
    # пропускаем слова, в которых менее 4 уникальных символов
    if len(set(word)) < 4:
        continue
    # пропускаем слова, которые встретились в тексте менее 2 раз
    if word_counter[word] <= 2:
        continue
    # слова прошедшие фильтрацию, добавляем в список filter_words
    filter_words.append(word)

# сортируем по алфавиту методом sort
filter_words.sort()

# выводим в консоль
for i in filter_words:
    print(i)
