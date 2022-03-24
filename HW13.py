
history = {"Kosya", "Masha", "Danila", "Vanya", "Egor"}
biology = {"Sveta", "Vanya", "Sergei", "Marina", "Kostya", "Masha", "Anton"}
sport = {"Anton", "Nikolay"}

h_b = history.intersection(biology)
print(" history and biology:", h_b)

plus_sport = h_b.intersection(sport)
print("all lessons:", plus_sport)

s_b = sport.intersection(biology)
print("sport+biology:", s_b)

all = history | biology | sport
print(sorted(all))
