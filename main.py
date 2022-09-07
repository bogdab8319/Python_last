
# def function_1(num1, num2):
#     for i in range(num1,num2):
#         if i%2==0:
#             print(i)
# function_1(1,10)


#     Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

# def draw_square(n, s, f):
#     r = s * n
#     if not f:
#         m = s + " " * (n - 2) + s
#     else:
#         m = r
#     print(r)
#     for i in range(n - 2):
#         print(m)
#     print(r)
#
#
# draw_square(5, "#", True)
# print("")
# draw_square(5, "*", False)


# def funk_square(length, symbol, switcher=False):
#     space = ' '
#     square = ''
#     symb_leng = len(symbol)
#     if switcher:
#         for i in range(length):
#             square = square + length * symbol + '\n'
#     else:
#         for i in range(length):
#             if i == 0 or i == (length - 1):
#                 square = square + (length * symbol) + '\n'
#             else:
#                 square = square + symbol + ((length - 2) * symb_leng * space) + symbol + '\n'
#     print(square)
#
# funk_square(3, '&&')
# funk_square(5, '**', True)
# funk_square(7, '- -')
# funk_square(8, '+', 'False')





#     def print_figura(length, weight, full):
#     if full:
#         for i in range(length):
#             print()
#             for j in range(weight):
#                 print('*', end='')
#     else:
#         for h in range(length):
#             for w in range(weight):
#                 if h == 0 or h == length - 1 or w == 0 or w == weight - 1:
#                     print('*', end='')
#                 else:
#                     print(' ', end='')
#             print()
#
# print_figura(6, 6, True)










