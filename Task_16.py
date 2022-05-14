# Задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

# Функция на получение целого числа с проверкой на ввод буквы
def get_number():
    while True:
        try:
            console_input = abs(int(input('Введите число: ')))
            return int(console_input)
        except ValueError:
            print("Is not a valid number.")


# Получаем число
n = get_number()

# Создаем пустой массив
massive = []

# Цикл в котором заполняется массив по формуле. Функция append добавляет новый элемент в конец.
for i in range(1, n+1):
    massive.append(1+(1/i)**i)
# Функцией sum считаем сумму массива, а командой .2f округляем вещественное число до двух символов
print(f'{sum(massive):.2f}')
