# Задача №38
# Напишите программу, удаляющую из текста все слова, содержащие "абв".


text = "забвение! программа Зимбабве удаляющая Абв из текста слова"
text_list = text.split()
result = list(filter(lambda x: not "абв" in x.lower(), text_list))
print(result)

for indx, val in enumerate(text):
    if val == " ":
        print(indx)
