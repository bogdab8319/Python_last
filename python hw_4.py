
 # Задание №1

first_num= int(input('Введите первое число'))
second_num= int(input('Введите второе число'))

while first_num< second_num:
    print(first_num )
    first_num += 1
    if first_num % 7 == 0:
        print(first_num, ' Число кратное 7')


# Задание  № 2

first_num= int(input('Введите первое число'))
second_num= int(input('Введите второе число'))

while first_num< second_num:
     num= print(first_num,' Все числа диапазона' )
     first_num += 1

     if first_num%7==0:
         print(first_num,' Все числа диапазона','  Все числа кратніе 7')
     elif first_num % 5== 0:
         print(first_num, ' Все числа диапазона', '  Все числа кратніе 5')
for i in range(second_num):
         print(second_num - i,'Диапазон в убівающем порядке')


# Задание № 3


num_1 = int(input('Введите первое число'))
num_2 = int(input('Введите второе число'))

while num_1 < num_2:
    print(num_1, end=" ")
    num_1 += 1

    if num_1 % 3 == 1:
        print(' Fizz')
    elif num_1 % 5 == 1:
        print(' Buzz')
    if num_1 % 3 == 1 and num_1 % 5 == 1:
        print(' Fizz  Buzz' )
    else :
       print()


# Задание №4


num_first = int(input('Введите первое число'))
num_second = int(input('Введиде второе число'))
sum = 0
sumch = 0
sum9 = 0
for i in range(num_first+1, num_second):
    if i % 2 != 0:
     sum += i

    if i % 2 == 0:
     sumch += i

    if i % 9 == 0:
      sum9 += i
      print(sum9, ' Сумма кратніх 9')
      print(sum, ' Сумма нечетніх')
      print(sumch, ' Сумма четніх')

# Задание № 5

while True :
   a = int(input('Введите число'))

   if a>0:
     print(' Number is positiv')
   elif a<0:
     print(' Number is negativ')
   elif a==0:
     print(' Number is equel to zero')
   if a==7:
    print('Good bye')
    exit()


# Задание № 6

masiv=[]
while True:
  num= int(input('Input number'))
  masiv.append(num)
  if num==7:
    print('Сумма чисел',sum(masiv))
    print('Максимальное число',max(masiv))
    print('Минимальное число',min(masiv))
    exit()

# Модуль 3. Циклы.
# Часть 3            Не успел  разобраться, рано утром уезжаю в командировку (((


















