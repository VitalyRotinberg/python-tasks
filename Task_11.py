#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

def try_parse():
    while True:
        try:
            console_input = abs(int(input('Введите число: ')))
            return int(console_input)
        except ValueError:
            print("Is not a valid number.")

list = []
N = try_parse()
for i in range(N):
    if i % 2 == 0:
        list.append(3**i)
    else:
        list.append(-3**i)
print(list)  
