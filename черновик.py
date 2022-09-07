# def mobifuname (userName):
#     newName = userName.upper()
#     return newName
# name = input(" input your name :")
# print(mobifuname(name))

# def modifyName(userName):
#     newName = userName.upper()
#     print("Hello!")
#     return newName
#     print("Hello!")
# name = input("Input your name:")
# print(modifyName(name))


# users=[['user1', '111'],['user2', '2222'],['user3', '33333']]
#
# def printInfo(*clients):
#     for i in range(len(clients)):
#         if i==0:
#          print("login{}".format(clients[i]))
#         elif i==1:
#          print("pass:{}".format(clients[i]))
#     for user in users:
#         printInfo(*user)


# pizzaTypes=['Neapolitan','Sicilian','Detroit','New York-Style']
# print(pizzaTypes)
# def modifyPizzaTypes(pizzaTypes):
#     return pizzaTypes+' Pizza'
# pizzaNames=list(map(modifyPizzaTypes,pizzaTypes))
# print(pizzaNames)


# def askAdditionalInfo(queryStr):
#     infoInd=1
#     infoList=[]
#     while True:
#         infoName=input("Name of the {} #{}:".format(queryStr,infoInd))
#         if infoName=="":
#             print("No info. Input stopped.")
#             break
#         else:
#             infoList.append(infoName)
#              infoInd+=1
#
#
#     if len(infoList)>0:
#         if queryStr=='hobby':
#             print("You have {} hobbies.".format(infoInd-1))
#         elif queryStr=='programming languages':
#             print("You know {} programming languages.".format(infoInd-1))
#     else:
#         print("You have no info at all")


# def askPersonalInfo():
#     while True:
#         firstName=input("Your first name:")
#         lastName=input("Your last name:")
#         yearBirth=input("Your year of birth:")
#         gender=input("Your gender (M,F):")
#         if firstName=="" or lastName=="" or yearBirth== "" or gender== "" or gender not in ('F','M'):
#             print("Wrong data!")
#         else:
#             return firstName, lastName, yearBirth,gender
# def askAdditionalInfo(queryStr):
#     infoInd=1
#     infoList=[]
#     while True:
#         infoName=input("Name of the {} #{}:".format(queryStr,infoInd))
#         if infoName=="":
#             print("No info. Input stopped.")
#             break
#         else:
#             infoList.append(infoName)
#             infoInd+=1
#     if len(infoList)>0:
#         if queryStr=='hobby':
#             print("You have {} hobbies.".format(infoInd-1))
#         elif queryStr=='programming languages':
#             print("You know {} programming languages.".format(infoInd-1))
#     else:
#         print("You have no info at all")
#     return infoList
# userInfo=[]
# userInfo.append(askPersonalInfo())
# userInfo.append(askAdditionalInfo('hobby'))
# userInfo.append(askAdditionalInfo('programming languages'))
# print(userInfo)


# grupList= input(" Введите оценки студенту" )
# myList =[grupList]
# def mySort(myList):
#     for i in range(len(myList)):
#         if i in len(myList)>0 or i in len(myList)<= 12:
#             myList= True
#         else:
#             break
#
#
#
#
# print(myList)


# def grupNum():
#     while True:
#         userNum = float (input(' Input numbers : '))
#         userList[] =userNum
#         if userNum< 0 or userNum>12 :
#             print( "Wrong number ")
#         else:
#             return userNum
#
# ListNum = grupNum()
# print(ListNum)

#                 SortedFlag=False
#         if SortedFlag:
#                 break
# def newList (myList):
#     for index , elem in enumerate(myList ):
#         print(f"Оценки : {elem}")
# # print(mySort(grupList))
# print(newList(myList))


# userList = [int(i) for i in input( " Введите оценки через пробел !") ]
# print()

# userList= int(input("hghg"))
# num=[]
# while True:
#     try:
#         num.append(userList)
#         userList=int(input( 'number'))
#     except:
#         break
#     print(num)
#
# num = list(map(int, input('input').split()))
# print(num)
# myList = num
# numDel = int(input(' Введите оценку по счету которую хотите пересдать '))
#
# del myList[numDel]
# print(myList)
# numApp = int(input("Введите оценку"))
# item = numApp
# numIndex = int(input(" Введите оценку по счету , каку хотите перездать"))
# index = numIndex
# myList.insert( index ,item)
# print(myList)



# class Test:
#     def __init__(self):
#         self.i = 5
#         self.f = 3.5
#
#     def __int__(self):
#         return self.i
#
#     def __float__(self):
#         return self.f
#
#
# t = Test()
#
# print(int(t))
# print(float(t))

class Person:
    __firstname = str()
    __lastname = str()
    __phone = str()

    def __init__(self, firstname: str, lastname: str, phone: str):
        self.set_firstname(firstname)
        self.set_lastname(lastname)
        self.set_phone(phone)

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_phone(self):
        return self.__phone

    def set_firstname(self, firstname: str):
        self.__firstname = firstname.capitalize()

    def set_lastname(self, lastname: str):
        self.__lastname = lastname.capitalize()

    def set_phone(self, phone: str):
        self.__phone = phone

    def set_firstname_godmode(self, firstname: str):
        self.__firstname = firstname

    def __str__(self):
        return f'{self.__firstname} {self.__lastname} {self.__phone}'

    def to_file(self, filename: str):
        with open(filename, 'a') as file:
            file.write(self.__str__() + '\n')

    @staticmethod
    def from_file(filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            return Person(res[0], res[1], res[2])
            # self.set_firstname(res[0])
            # self.set_lastname(res[1])
            # self.set_phone(res[2])


class Student(Person):
    __group = str()

    def __init__(self, firstname: str, lastname: str, phone: str, group: str):
        super().__init__(firstname, lastname, phone)
        self.set_group(group)

    def get_group(self):
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def __str__(self):
        return f'{super().__str__()} {self.__group}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_group(res[3])


class Teacher(Person):
    __subject = str()

    def __init__(self, firstname: str, lastname: str, phone: str, subject: str):
        super().__init__(firstname, lastname, phone)
        self.set_subject(subject)

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject: str):
        self.__subject = subject

    def __str__(self):
        return f'{super().__str__()} {self.__subject}'

    def from_file(self, filename: str):
        with open(filename, 'r') as file:
            res = file.readline().split()
            self.set_firstname(res[0])
            self.set_lastname(res[1])
            self.set_phone(res[2])
            self.set_subject(res[3])


li = []
obj = Person.from_file('test.txt')
print(obj)
li.append(Student('Ivasyk', 'Bulkin', 'trinolyatrulyalya', 'Python11'))
li.append(Student('Grigoiy', 'Terkin', '+387415874165', 'Python21'))
li.append(Student('Anna', 'Chechetkina', '+04478451235', 'C++14'))
li.append(Student('Svetlana', 'Bulkina', 'trinolyatrulyalya2', 'Python11'))
li.append(Student('Anatloiy', 'Fedorov', '0991234756', 'C++17'))

for i in li:
    print(i)

li[0].to_file('test.txt')

li[0].from_file('test.txt')

