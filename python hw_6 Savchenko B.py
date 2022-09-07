

# Задание № 2


text = input(" input words")
text_1 = text.lower()
listold = list(text.split())
listnew = list(text_1.split())
reserve_words = input("input reserve words").split()

for i in range(len(listnew)):
    for j in reserve_words:
        if j in listnew[i]:
            listold[i] = listnew[i].upper()
print('   '.join(listold))



# Задание№ 1

str=input(" input string")
if str!= str[::-1]:
    print("Строка Палиндр")
else:
    print("Строка не Палиндр")


# Задание№ 3

text = input("Input text")
print(len([i for i in text.split(".")]))






