# CodeForces task 118A
# Andrey Pompeev 20.06.2017

forbidden_letters = ("a", "o", "y", "e", "u", "i")
string = input().lower()
result_string = ''

for i in string:
    if i in forbidden_letters:
        pass
    else:
        result_string += ('.' + i)

print(result_string)
