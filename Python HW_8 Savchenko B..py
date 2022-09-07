

# Заданме №2     Написать программу «успеваемость». Модуль 7. Сортировка и поиск.

from  functools import reduce

num = list(map(int, input('Введите 10 оценок через пробел , от 1 до 12 ').split()))
print(num)
myList = num
numDel = int(input(' Введите оценку по счету которую хотите пересдать '))

del myList[numDel]
print(myList)
numIndex = int(input(" Введите оценку по счету , каку хотите перездать"))
index = numIndex
numApp = int(input("Введите новую оценку"))
item = numApp
myList.insert( index ,item)
print(myList)


myList_len = len(num)
myListSRB = reduce(lambda x,y: x+y, num)/ myList_len
print(" Средний балл: ")
print( myListSRB ,1)



def Sort_myList(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-1-i):
            if myList[j]>myList[j+1]:
                temp= myList[j]
                myList[j]=myList[j+1]
                myList[j+1]=temp
Sort_myList(num)
print("Отсортированній список:")
def printList(myList):
    for index, elem in enumerate(myList):

        print( f"   {index}:   {elem} Баллов")

printList(num)



# Задание № 3


def bsort(myList_P):
    n = len(myList_P)
    k, c = 1, 0
    while True:
        cc = 0
        for i in range(n - k):
            if myList_P[i] > myList_P[i + 1]:
                cc += 1
                myList_P[i], myList_P[i + 1] = myList_P[i + 1], myList_P[i]
        c += cc
        k += 1
        if cc == 0:
            break
    # print(*myList_P)
    print("Количество шагов : ",c)


# dummy = input()
myList_P = list(map(int, input().split()))
bsort( myList_P)
print( myList_P)