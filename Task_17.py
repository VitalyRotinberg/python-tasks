# 17.	Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

# Функция на получение целого числа с проверкой на ввод буквы
def get_number():
    while True:
        try:
            console_input = abs(int(input('Введите значения для крайних точек: ')))
            return int(console_input)
        except ValueError:
            print("Is not a valid number.")

# Получаем число с помощью функции
n = get_number()

# Создаем массив в котором будут храниться точки
elements = []

# Создаем результирующую переменную для произведения элементов
mult = 1

# Создаем переменную f, командой open открываем файл с модификатором r, для чтения
f = open('file.txt', 'r')

# Заполняем массив точками
for i in range(-n, n+1):
    elements.append(i)
print(elements)

# С помощью цикла умножаем элементы на указанных позициях в файле
for line in f:
    mult = mult * int(elements[int(line)])

print(mult)

# Закрываем файл
f.close()