# CodeForces task 231A
# Andrey Pompeev 20.06.2017 14:00

n = int(input())
tasks = 0

for _ in range(n):
    people_sure = sum(list(map(int, input().split(' '))))
    if people_sure > 1:
        tasks += 1
print(tasks)
