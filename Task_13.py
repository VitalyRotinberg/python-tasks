# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

a = "123asd"
b = "123asd123qwe123asd123asd123asdasd"

ind = 1
count = 0
while ind != -1:
    ind = b.find(a)
    if ind >= 0:
        count += 1
    b = b[ind+1:]

print(count)