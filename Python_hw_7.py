
import random

list_1 = []
list_2 = []
list_both = []
list_sovm_bp = []
list_sovm_sp = []
list_unick = []
list_min_max = []

lenght = random.randint(0,10)

for i in range(lenght):
    element_1 = random.randint(0,20)
    list_1.append(element_1)

    element_2 = random.randint(0,20)
    list_2.append(element_2)

    list_both = [list_1 + list_2]

    if element_1 == element_2:
        list_sovm_bp.append(element_1)
        list_sovm_sp.append(element_1,element_2)
    # не могу найти содержащий элементы  общие для двух списков; вібивает ошибку

    if element_1 != element_2:
        list_unick.append(element_1)
    elif element_2 != element_1:
        list_unick.append(element_2)

list_min_max.append(min(list_1))
list_min_max.append(max(list_1))
list_min_max.append(min(list_2))
list_min_max.append(max(list_2))



print(list_1," Первий список")
print(list_2, "Второй список")
print(" элементы обоих списков",list_both)
print("уникальные элементы",list_unick)
print("элементы обоих списков без повторений",list_sovm_bp)
print(" минимальное и максимальное значение", list_min_max)
print("содержащий элементы общие для двух списков;", list_sovm_sp)



