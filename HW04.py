"""
Найдите значение выражений
а) 0 или 1 и не (0 или 1)
б) 1 или 0 и 1 и 1 или 1
в) ((1 или 0) и (1 и 1))
г) ((А или 0) или В и 1) и 0
"""

A = 0
B = 0

f1 = 0 or 1 and not (0 or 1)
f2 = 1 or 0 and 1 and 1 or 1
f3 = ((1 or 0) and ( 1 and 1))
f4 = ((A or 0) or B and 1) and 0

print("f1 = ", f1)
print("f2 = ", f2)
print("f3 = ", f3)
print("f4 = ", f4)