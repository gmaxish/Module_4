
spisok = [5, 6, 3, 11, 4, 9, 2, 1, 10, 7]

max_spisok = max(spisok)
print('Max value is: ', max_spisok)

index_max_spisok = spisok.index(max_spisok) + 2
print("Index of max value is: ", index_max_spisok)

del spisok[index_max_spisok: len(spisok)]
print(spisok)