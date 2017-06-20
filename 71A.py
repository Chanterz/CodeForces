# CodeForces task 71A
# Andrey Pompeev 20.06.2017

n = int(input())

for i in range(n):
    inp = input()
    if len(inp) > 10:
        print("{}{}{}".format(inp[0], len(inp) - 2, inp[-1]))
    else:
        print(inp)
