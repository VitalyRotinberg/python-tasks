# Реализовать алгоритм перемешивания списка. 

# Подключаем библиотеку для класса random
import os
import random
os.system("cls")

# С помощью randint заполнили список на 10 элементов числами
list = [random.randint(1, 101) for item in range(10)]
print(list)

# функцией shufle перемешали список в рандомном порядке
random.shuffle(list)
print(list)