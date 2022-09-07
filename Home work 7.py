


# Задание №2
list=[5,9,12,45,61,18,39,9,15,-3]
def list_min(list):
    if len(list)==0:
        return None
    if len(list)==1:
        return list[0]
    else: s=min(list[1:])
    return s if s < list[0] else list[0]

print(list_min(list))





 # Задание№ 3

def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3,  2):
        if k%i==0:
            return False

    return True
print(isitPrime(15))






# Задание № 4


list=[1,13,25,53,62,74,89,37,18,42]

def delete_number(list):
    for i in range(4, len(list)):
        # удаляем из списка "4" индекс
        if list[i]%2 == 0:
            list.remove(list[i])
        return list
print(delete_number(list))



# Задание № 1


def myListV_1  (a,b,c,d):
    return (a+b)*(c+d)
def myListV_2 (a,b,c,d):
    return (a+b)/(c+d)
def myListV_3 (a,b,c,d):
    return (a + b) / (c- d)
def Chois_user (k):
    if "1":
        return myListV_1
    elif "2":
        return myListV_2
    elif "3":
        return myListV_3
x=7
y=2
z=4
r=1
for i in range(3):
    user_new = input(" your chois: ")
    myCalection= Chois_user(user_new)
    print(myCalection(x,y,z,r) )


