

#Задание №1
leg_a=int(input('Введите первое число'))
leg_b= int(input('Введите второе число'))
leg_c= int(input('Введите третье число'))

print('Вывод :'+str(leg_a)+ str(leg_b)+str(leg_c))


#Задание №3
Summa = int(input(' Введите количество метров: '))
dm= print(str( Summa*10) + ' Количество дециметров')
sm= print(str(Summa*100) +" Количесво сантиметров")
mm= print(str(Summa*1000) +" Количесво миллиметров")
ml_l= print(str(Summa//1.6) +" Количесво сухопутных миль")
ml_v=print(str(Summa//1.852) +" Количесво морских миль")



#Задание№2


number= int(input('Введите четырех число'))
e = int(number //1000)
d = int(number//100)%10
c = int(number //10)%10
b = int(number %10)

print(b*c*d*e)



#Задание№4


ab = input("Длина первого катета: ")
ac = input("Длина второго катета: ")
ab = float(ab)
ac = float(ac)
bc = (ab ** 2 + ac ** 2)

print((ab * ac) / 2)




#Задание№5

a= input('Введите число :')
b= a[::-1]
print(b)
