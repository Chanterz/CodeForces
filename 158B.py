# CodeForces task 158B
# Andrey Pompeev 20.06.2017 21:16
from math import *

max_car_capacity = 4
current_amount_of_passengers = 0
n = int(input())
s = list(map(int, input().split(' ')))

groups = [0, 0, 0, 0]
s.sort()

for i in s:
    groups[i - 1] += 1
s = groups.copy()

del (groups)

car_amount = s[3]
s[3] = 0

t = min(s[2], s[0])
car_amount = car_amount + t
s[2] = s[2] - t
s[0] = s[0] - t

car_amount = car_amount + trunc(s[1] / 2)
s[1] = s[1] - 2 * trunc(s[1] / 2)

t = min(s[1], trunc(s[0] / 2))
car_amount = car_amount + t
s[1] = s[1] - t
s[0] = s[0] - 2 * t

car_amount = car_amount + trunc(s[0] / 4)
s[0] = s[0] - 4 * trunc(s[0] / 4)

car_amount = car_amount + s[2]
s[2] = 0

t = min(s[1], s[0])
car_amount = car_amount + t
s[1] = s[1] - t
s[0] = s[0] - t

car_amount = car_amount + trunc(s[0] / 3)
s[0] = s[0] - 3 * trunc(s[0] / 3)

car_amount = car_amount + s[1]
s[1] = 0

car_amount = car_amount + trunc(s[0] / 2)
s[0] = s[0] - 2 * trunc(s[0] / 2)

car_amount = car_amount + s[0]
s[0] = 0

print(car_amount)
