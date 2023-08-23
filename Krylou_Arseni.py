# Дано предложение:Не знаю,как там в Лондоне,я не была.\
# Может,там собака-друг человека. А у нас управдом-друг человека!
# Шаг 1-Количество символов
sentence = "Не знаю, как там в Лондоне, я не была.\
Может, там собака-друг человека. А у нас управдом-друг человека! "
character_count = len(sentence)
print(f"Шаг 1 Количество символов: {character_count}")


# Шаг 2-Переворот строки
def reverse_string(input_string):
    return input_string[::-1]


input_string = "Не знаю, как там в Лондоне, я не была.\
Может, там собака-друг человека. А у нас управдом-друг человека!"
reversed_string = reverse_string(input_string)
print(f"Шаг 2 перевёрнутая сторка: {reversed_string}")

# Шаг 3-Большие буквы
sentence = "Не знаю, как там в Лондоне, я не была. \
Может, там собака-друг человека. А у нас управдом-друг человека!"

uppercase_sentence = sentence.upper()
print(f"Шаг 3 Вывод большими буквами: {uppercase_sentence}")


# Шаг 3-Прописные буквы
def lowercase_string(input_string):
    return input_string.lower()


input_string = "Не знаю, как там в Лондоне, я не была.\
 Может, там собака-друг человека. А у нас управдом-друг человека!"
lowercase_string = lowercase_string(input_string)
print(f"Шаг 4 Вывод прописными буквами:{lowercase_string}")

# Шаг 5-Подсчёт вхождений в строку нд,ам и о
def count_occurrences(input_string, substrings):
    count = 0
    for substring in substrings:
        count += input_string.count(substring)
    return count

input_string = "Не знаю, как там в Лондоне, я не была.\
 Может, там собака-друг человека. А у нас управдом-друг человека!"
substrings = ["нд", "ам", "о"]
occurrence_count = count_occurrences(input_string, substrings)
print(f"Шаг 5 Подсчёт вхождений нд, ам, о в строку: {occurrence_count}")

#Шаг 7-Разворот предложения
def reverse_sentence(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input_string = "Не знаю, как там в Лондоне, я не была.\
 Может, там собака-друг человека. А у нас управдом-друг человека!"
reversed_sentence = reverse_sentence(input_string)
print(f"Шаг 7 Разворот строки:{reversed_sentence}")

# Шаг 8-Вывод исходного текста
print("Шаг 8 вывод иходного текста: Не знаю,как там в Лондоне,я не была.\
Может,там собака-друг человека. А у нас управдом-друг человека!")