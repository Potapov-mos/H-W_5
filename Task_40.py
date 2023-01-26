# Задача №40.

#  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.


def encode(text):
    result = ""
    count = 0
    prev_char = text[0]
    for char in text:
        if char != prev_char:
            result += f"{count}{prev_char}"
            prev_char = char
            count = 1
        else:
            count += 1
    else:
        result += f"{count}{prev_char}"
    return result


def decode(text):
    result = ""
    digit = True
    count = 0
    for char in text:
        if digit:
            count = int(char)
            digit = False
        else:
            result += count*char
            digit = True
    return result

text = 'aaaabbbbbcccee'
print(f'Исходный текст: {text}')
encode_text = encode(text)
decode_text = decode(encode_text)
print(f'Результат сжатия данных: {encode_text}')
print(f'Результат сжатия данных: {decode_text}')
