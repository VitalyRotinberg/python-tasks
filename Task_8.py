# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

def is_number():
    while True:
        try:
            a, b = map(float, input("Введите координаты x,y через пробел: ").split())
            return float(a), float(b)
        except ValueError:
            print("Are not valid coordinates.")


x, y = is_number()

if x == 0 and (y < 0 or y > 0):
    print('Точка на оси X')
elif y == 0 and (x < 0 or x > 0):
    print('Точка на оси Y')
if x > 0:
    if y > 0:
        print('Первая четверть')
    elif y < 0:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    elif y < 0:
        print('Третья четверть')
