




# Задание № 1


while True:
    number = int(input('input number'))
    answer = 'Simple'
    for i in range( 2, number//2):
        if number % i==0:
             answer= 'Not simple'
    print(f' This number is {answer}')





# Задание № 2


for i in range(1, 10+1):
   for j in range(1, 10+1):
       print(i, '*', j, '=', i * j, end='\t\t')
   print()
   #  eсли закоментировать print() будет вівод в строку( как в задании)




# Задание № 3

while True:
    num=int(input('input number'))

    for i in range(1,10+1):

      for j in range(num, num+1):
             print(i, '*', j, '=', i * j, end='\t\t')
    print()


# Часть  № 5





# Б

for h in range(10):
    for w in range(h+1):
        print('*', end=" ")
    print()

# В

num=10
k=(2*num)-2
for h in range( num, -1,-1):
    for w in range(k,0,-1):
        print(end=" ")
    k=k+1
    for w in  range(0,h,+1):
          print("*", end=" ")
    print( " ")


# Г


num_2 =10
m= (2* num_2)-2
for h in range(0,num_2):
    for w in range(0,m ):
        print(end=" ")
    m = m-1
    for w in range(0, h+1):
        print("*", end=" ")
    print( )




#   Д

size=10
k=(2*size)-2
for h in range( size, -1,-1):
    for w in range(k,0,-1):
        print(end=" ")
    k=k+1
    for w in  range(0,h+1):
        print("*", end=" ")
    print(  )

for h in range(0, size):
    for w in range(0, k ):
        print(end=" ")
    k = k-1
    for w in range(0, h+1):
        print( "*", end=" ")
    print( )



# И

num_1= 10
s=num_1
for h in range(num_1,0,-1):
    for w in range(0):
        print( end=" ")
    s=s-1
    for w in range(h):
        print("*", end=" ")
    print()







