# CodeForces task 112AA
# Andrey Pompeev 20.06.2017 14:27

string_one = input().lower()
string_two = input().lower()

code = 0

for i, j in zip(string_one, string_two):
    if i < j:
        code = -1
    elif i > j:
        code = 1

print(code)