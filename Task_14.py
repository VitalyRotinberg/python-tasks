# Подсчитать сумму цифр в вещественном числе

# Подключаем библиотеку для класса random
import os
import random
os.system("cls")


# Задаем случайное вещественное число из указанного диапазона
a = random.uniform(1, 1000)
print('Заданно число', a)

# Переводим в строку, меняем функцией replace точку на пустой символ (убираем точку) 
a = str(a).replace('.', '')
print(a)

# При выводе сразу же с помощью функции sum суммируем переведенные в int числа
# функция map переводит каждый символ строки отдельно, и его же считает. 
print('Сумма цифр =',  sum(map(int, a)))