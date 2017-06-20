# CodeForces task 96A
# Andrey Pompeev 20.06.2017 14:12

import sys

inp = input()

first_team = inp.split('1')
second_team = inp.split('0')

first_team = list(map(len, first_team))
second_team = list(map(len, second_team))

for i in first_team:
    if i >= 7:
        print('YES')
        sys.exit()
for i in second_team:
    if i >= 7:
        print('YES')
        sys.exit()
print('NO')
