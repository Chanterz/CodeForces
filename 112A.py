# CodeForces task 112A
# Andrey Pompeev 20.06.2017 14:27

string_one = input().lower()
string_two = input().lower()

code = 0


if string_one < string_two:
    code = -1
elif string_one > string_two:
    code = 1

print(code)