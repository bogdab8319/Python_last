


# # # Задание № 1.2
# #
# plaers={'Michle Jordan':'201 sm',
#         'Magic Jonson':'205 sm',
#         'Deenis Rodman':'205 sm',
#         'Scotti Pipen':' 207 sm',
#         ' Stanislav Medvedenko': '210 sm',
#         'Alexiy Len':' 216 sm'
#         }
#
# print('Old list', plaers )
#
# for key, val in plaers.items():
#     print( f'{key}___{val}')
# sortPlaers= sorted(plaers.items(),key=lambda x:x[0])
# for element in sortPlaers:
#     print('Sorter List ',element)
#
#
# newPlaer_1=input(' What plaers you wont to add?')
#
# if newPlaer_1 != "":
#     infoValue= input (f'input value of the plaer {newPlaer_1}')
#     if infoValue!= "":
#         plaers[newPlaer_1]=infoValue
#     else:
#         print(f'No value for the plaer{newPlaer_1}')
#
#     for key,val in plaers.items():
#         print(f' List chenget_-** {key}___{val}')
#
#
#
#
#
#
# for key, val in plaers.items():
#     print( f'{key}___{val}')
# sortPlaers= sorted(plaers.items(),key=lambda x:x[0])
# for element in sortPlaers:
#     print('Sorter List ',element)
#
# plaersUpdate= input(' Input name plaers Up')
# plaersUpdate_1= plaersUpdate
# isNameUpdate=False
# for i in plaers:
#     if plaers.get(plaersUpdate):
#         # plaers.update(plaersUpdate_1)
#         print(plaers)
#
# plaers.update([('Stanislaav Mihailyk','201 sm'),
#                ('Alexiy Pecherov','215 sm')])
# print('list ',plaers)
# plaers.update([('Michael Jordan','198 sm')])
# # # #                                                     #  Джордону изменил рост и коркктно нарисал Имя
# print('List chenget',plaers )
# # # #
# # # #
# # # #
# keyNameDel= input(' Input plaer to delele')
# keyNameDel_1=keyNameDel
# isNameDelFound=False
# for plaer in plaers :
#     if plaers. get(keyNameDel):
#         print('Plaers is  found')
#         del plaers[keyNameDel_1]
#         print('Delete of list',plaers)
#         isNameDelFound= True
#         break
# if isNameDelFound==False:
#     print('Plaers is not found !')
# # #                                                 # Потратил 3 часа , но Меджика удалил с єтого словаря )))))
# # #
# # #
# # #                                                   # Поиск украинцев в списке
# #
# #
# keyName= input( ' Input plaers in ukraine')
# isPlaerFound=False
# for plaer in plaers :
#     if  plaers.get(keyName):
#         print('Plaers is  found')
#
#         print(f' - {key}:{val}')
#         isPlaerFound= True
#         break
#
# if isPlaerFound== False:
#     print('Plaers is not found !')
#




    # Задание № 2  Требуется реализовать возможность добавления, удаления, поиска, замены данных.


bookWords={'word': "слово", 'red': 'читать','pen': 'ручка','tea':'чай', 'man': 'мужчина','wooman': 'женщина','list': 'список',
       'windows': 'окна','user':'пользаватель'
      }

for key, val in bookWords.items():
    print( f'{key}___{val}')
sortBookWords= sorted(bookWords.items(),key=lambda x:x[0])
for element in sortBookWords:
    print(element)
                                                                       # Отсортировал по ключу

keyEng= input('Input English word')

isElemFound= False
for bookWord in bookWords:
    if bookWords.get(keyEng):
        print(f' Word is found ^: {keyEng}')
        isElemFound=True
        break

if isElemFound==False:
    print(' World is not found!')
                                           # Как то каряво получилось !!!!


newWord=input(' What word you wont to add?')

if newWord != "":
    infoValue= input (f'input value of the word {newWord}')
    if infoValue!= "":
       bookWords[newWord]=infoValue
    else:
        print(f'No value for the word{newWord}')

    for key,val in bookWords.items():
        print(f' List chenget_-** {key}___{val}')


keyWordDel= input(' Input word to delele')
keyWordDel_1=keyWordDel
isWordDelFound=False
for key in bookWords :
    if bookWords. get(keyWordDel):
        print('word is  found')
        del bookWords[keyWordDel_1]
        print('Delete of list',bookWords)
        isWordDelFound= True
        break
if isWordDelFound==False:
    print('Word is not found !')


                                                               # Замена данніх

key_Word_Chenge = input( " Введите слово на замену 1:")



if key_Word_Chenge != "":
    infoValue_Chenge = input (f'Введите слово на замену 2: {key_Word_Chenge}')
    if infoValue_Chenge != "":
       bookWords[key_Word_Chenge] = infoValue_Chenge
       print(infoValue_Chenge)
       bookWords.update(key_Word_Chenge)
    else:
        print(f'No value for the plaer{key_Word_Chenge}')

    for key,val in bookWords.items():
        print(f' List chenget_-** {key}___{val}')



# cart = {'apples': 2, 'oranges': 1}
# addon = {'oranges': 5, 'lemons': 3}
# cart.update(addon)
# cart  # {'apples': 2, 'oranges': 5, 'lemons': 3}