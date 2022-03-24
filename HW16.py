hishniki = {"Тигры", "Львы", "Волки", "Медведи"}
ptici = {"Попугаи", "Совы", "Пеликаны", "Пингвины", "Орлы", "Фламинго"}
travoyadnie = {"Кролики", "Слоны", "Жирафы", "Зебры", "Носороги", "Косули"}

all = hishniki | ptici | travoyadnie
print(sorted(all))

mlekopit = hishniki | ptici
print(mlekopit)

ptici.remove("Совы")
ptici.remove("Орлы")
print(ptici)

ptici.add("Журавли")
ptici.add("Пеликаны")
ptici.add("Павлины")
print(ptici)

new_all = hishniki | ptici | travoyadnie
print(sorted(new_all))
