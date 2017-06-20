# CodeForces task 158A
# Andrey Pompeev 20.06.2017

inp = input().split(" ")
inp = list(map(int, inp))
results = list(map(int, input().split(' ')))

i = 0

for j in results:
    if j >= results[inp[1] - 1] and j > 0:
        i += 1
    else:
        break
print(i)
