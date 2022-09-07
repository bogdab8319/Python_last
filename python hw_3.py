#Задание №1

first_name=1
second_name=100
var= int(input('Введите число от 1 до 100'))

if var%3==0:
    print("Fizz")
elif var%5==0:
    print('Buzz')
elif var%3==0 and var%5==0 :
    print('Fizz Buzz')
else:
    print('Введите другое число')
if var>=first_name and var<=second_name:
    print('Ві ввели коректное число')
else:
    print('Ошибка, не верній ввод числа')



#Задание №2


nam= int(input('Введите число'))
res= int(input('Введите 1 для возведения в степень "0"\n'
               'Введите 2 для возведения в степень "1"\n'
               'Введите 3 для возведения в степень "2"\n'
                'Введите 4 для возведения в степень "3"\n'
               'Введите 5 для возведения в степень "4"\n'
               'Введите 6 для возведения в степень "5"\n'
               'Введите 7 для возведения в степень "6"\n'
               'Введите 8 для возведения в степень "7"'))
print( 'Результат: ')
if res==1:
    print('Условие не віполнимо')
elif res==2:
    print(nam**1)
elif res==3:
    print(nam**2)
elif res==4:
    print(nam**3)
elif res==5:
    print(nam**4)
elif res==6:
    print(nam**5)
elif res==7:
    print(nam**6)
elif res==8:
    print(nam**7)


#Задание №3

summa= int(input('Введите сумму для звонка'))
UMC=2
LIFE=5
res= int(input('Введите 1. для звонка с UMC на LIFE\n'
               'Введите 2. для звонка с LIFE на UMC\n'
               'Введите 3. для звонка с UMC на UMC\n'
               'Введите 1. для звонка с LIFE на LIFE\n'))
print('Остаток минут: ')
if res==1:
    print(summa/(UMC+(LIFE/100*20)))
elif res==2:
    print(summa/(LIFE+(UMC/100*35.3)))
elif res==3:
    print(summa/UMC)
elif res==4:
    print(summa/LIFE)



#Задача №4


salary=200
prize=200
first_maneger=int(input('Введите уровень продаж первого менеджера'))

if first_maneger<500 :
    print(first_maneger/(100*0.03)+salary)
elif 500<first_maneger<1000 :
    print(salary+first_maneger/(100*0.05))
elif first_maneger>1000:
    print(salary+first_maneger/(100*0.058))

second_manedger=int(input('Введите уровень продаж второго менеджера'))
if second_manedger<500 :
    print(second_manedger/(100*0.03)+salary)
elif 500<second_manedger<1000 :
    print(salary+second_manedger/(100*0.05))
elif second_manedger>1000:
    print(salary+second_manedger/(100*0.058))

third_manedger= int(input('Введите уровень продаж третьего менеджера'))
if third_manedger < 500:
    print(third_manedger/(100*0.03)+salary)
elif 500 < third_manedger < 1000:
    print(salary+third_manedger/(100*0.05))
elif third_manedger > 1000:
    print(salary+third_manedger/(100*0.058))
    
                 # Не могу правельно посчитать ЗП+ПРОЦЕНТ+ ПРЕМИЯ

if first_maneger > second_manedger > third_manedger:       # не правельно, голова кипит , не хватило времени додумать:((
    print(salary+prize+first_maneger)
if first_maneger < second_manedger > third_manedger:
    print(salary+prize+second_manedger)
if first_maneger < second_manedger < third_manedger:
    print(salary + prize + third_manedger)

