spisok = [5, 6, 3, 11, 4, 9, 2, 1, 10, 7]

max_value_spisok = max(spisok)
min_value_spisok = min(spisok)

index_max = spisok.index(max_value_spisok)
index_min = spisok.index(min_value_spisok) + 1

print("Max value is:", max_value_spisok)
print("Min value is:", min_value_spisok)
print("Index of Max value is:", index_max)
print("Index of Min value is:", index_min)

del spisok[index_max: index_min]

print(spisok)