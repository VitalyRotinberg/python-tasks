# Найти расстояние между двумя точками пространства

import math
import random

xa = random.randrange(-10, 11)
ya = random.randrange(-10, 11)
za = random.randrange(-10, 11)
xb = random.randrange(-10, 11)
yb = random.randrange(-10, 11)
zb = random.randrange(-10, 11)

distance_between_points = round(math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2), 1)

print(f"Точка a: {xa, ya, za} \nТочка b: {xb, yb, zb}")
print(f"Дистанция между точками {distance_between_points}.")