# Написать программу получающую набор произведений от 1 до N

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

# Создал результирующую переменную, через которую буду выводить набор произведений
res = 1

# Циклом распечатываю набор произведений
for i in range(1, n+1):
    res = res * i
    print(res, end=' ')
