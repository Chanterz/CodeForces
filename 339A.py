# CodeForces task 339A
# Andrey Pompeev 20.06.2017 21:06

inp = input().split('+')
inp.sort()

output = inp[0]

for i in inp[1:]:
    output += '+{}'.format(i)
print(output)
