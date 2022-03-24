first = {1, 2, 3, 4, 5, 6, 7}
second = {4, 5, 6, 7, 9, 0, 3}
third = {5, 7, 11, 35, 65, 3}

A = first.intersection(second)
B = A.intersection(third)
print(B)

r = (first - second) - third
print(r)
r1 = (first - third) - (second - third)
print(r1)
print(r == r1)
