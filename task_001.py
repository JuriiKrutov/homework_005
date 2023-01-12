# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input()
exceptions = 'абв'
list = [i for i in text.split() if exceptions not in i.lower()]
print(*list, end=' ')