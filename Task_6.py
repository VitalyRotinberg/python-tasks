# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

def try_parse_int():
    while True:
        try:
            console_input = abs(int(input("Enter a weekday number: ")))
            return int(console_input)
        except ValueError:
            print("Is not a valid number.")


num = try_parse_int()

if num < 1 or num > 7:
    print('Вы ввели не день недели')
elif num == 6:
    print('Это суббота. День недели является выходным')
elif num == 7:
    print('Это воскресенье. День недели является выходным')
elif 1<= num and 6 > num:
    print('Вы ввели будный день недели')