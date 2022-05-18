# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

import os
os.system("cls")
list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(list)
str = input('Что будем искать?: ')
count = 0
for i in range(len(list)):
    if list[i] == str:
        count += 1
    if count == 2:
        print('Позиция второго вхождения равна ', i)
        break
if count != 2:
    print('-1')